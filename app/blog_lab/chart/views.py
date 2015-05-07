from app.blog_log.models import AccIP, ReqRecord
from django.utils import timezone
from django.http import HttpResponse
from app.decorater import api_times
from app.utils import encodejson
import datetime
import copy


def get_chart_message(req):
    body = {}
    now = timezone.now()
    start = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
    record_list = ReqRecord.objects.filter(create_time__gt=start).values('uri').distinct()
    day_rec_list = []
    for itm in record_list:
        rec = {}
        rec_count = ReqRecord.objects.filter(create_time__gt=start, uri=itm['uri']).count()
        rec['uri'] = itm['uri']
        rec['count'] = rec_count
        day_rec_list.append(copy.copy(rec))
    body['req_rec'] = day_rec_list
    return HttpResponse(encodejson(1, body), content_type="application/json")
