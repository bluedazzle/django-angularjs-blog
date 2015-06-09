from django.db import models
# Create your models here.


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)


    def serializer(self, time_format='timestamp', deep=False):
        # print self._meta.fields
        attr_list = [f.name for f in self._meta.fields]
        dic_list = {}
        if time_format == 'timestamp':
            date_func = datetime_to_timestamp
        elif time_format == 'utc':
            date_func = datetime_to_utc_string
        else:
            date_func = datetime_to_string
        # print attr_list
        for itm in attr_list:
            if isinstance(getattr(self, itm), models.Model):
                if deep:
                    dic_list[itm] = getattr(self, itm).serializer(time_format, deep)
            elif isinstance(getattr(self, itm), datetime.datetime):
                dic_list[itm] = date_func(getattr(self, itm))
            else:
                dic_list[itm] = getattr(self, itm)
        return dic_list

    class Meta:
            abstract = True


class AccIP(BaseModel):
    ip = models.CharField(unique=True, max_length=20)
    belong = models.CharField(max_length=50)
    total = models.IntegerField(default=0)
    day_count = models.IntegerField(default=0)
    black = models.BooleanField(default=False)

    def __unicode__(self):
        return self.ip


class ReqRecord(BaseModel):
    uri = models.CharField(max_length=100, default='')
    ip = models.ForeignKey(AccIP, related_name="records")

    def __unicode__(self):
        return self.uri


class BackLog(BaseModel):
    content = models.CharField(max_length=50)
    log_type = models.IntegerField()
    status = models.BooleanField(default=True)
    fail_message = models.CharField(max_length=500, default='')

    def __unicode__(self):
        return self.content