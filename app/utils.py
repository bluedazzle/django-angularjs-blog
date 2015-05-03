import random
import simplejson
import datetime
from django.db.models.query import QuerySet
from django.utils import timezone
from django.db import models
from django.core.paginator import Page
from PIL import Image, ImageDraw, ImageFont
import string
import time
import xmltodict
import copy
import os
from pytz import timezone as pytz_zone

BASE = os.path.dirname(os.path.dirname(__file__))


def isactive(lastactivetime, det=600):
    try:
        print lastactivetime
        nowt = datetime.datetime.utcnow()
        print nowt
        detla = nowt - lastactivetime
        if detla > datetime.timedelta(seconds=det):
            return False
        else:
            return True
    except Exception, e:
        except_handle(e)


def encodejson(status, body):
    tmpjson={}
    tmpjson['status'] = status
    tmpjson['body'] = body
    return simplejson.dumps(tmpjson)


def create_random_str(count=4):
    return string.join(random.sample('ZYXWVUTSRQPONMLKJIHGFEDCBA1234567890zyxwvutsrqponmlkjihgfedcba', count)).replace(" ", "")


def create_token(count=32):
    return string.join(random.sample('ZYXWVUTSRQPONMLKJIHGFEDCBA1234567890zyxwvutsrqponmlkjihgfedcba+=', count)).replace(" ", "")


def string_to_datetime(timestring, timeformat='%Y-%m-%d'):
    dateres = datetime.datetime.strptime(timestring, timeformat)
    dateres = dateres.astimezone(timezone.get_current_timezone())
    return dateres

def datetime_to_timestamp(datetimet):
    datetimet = datetimet.astimezone(timezone.get_current_timezone())
    return time.mktime(datetimet.timetuple())

def datetime_to_string(datetimet):
    time_str = datetimet.astimezone(timezone.get_current_timezone())
    return time_str.strftime('%Y-%m-%d %H:%M:%S')

def datetime_to_utc_string(datetimet):
    return str(timezone.localtime(datetimet))


def model_serializer(djmodels, datetime_format='timestamp', serializer='dict', include_attr=None,  except_attr=None, deep=False):
    if djmodels is None:
        return None
    # if datetime_format == 'timestamp':
    #     time_format_func = datetime_to_timestamp
    # elif datetime_format == 'string':
    #     time_format_func = datetime_to_string
    # else:
    #     time_format_func = datetime_to_timestamp
    result = []
    if isinstance(djmodels, models.Model):
        djmodels = [djmodels]
    if isinstance(djmodels, (QuerySet, list, Page)):
        for itm in djmodels:
            attr_list = itm.serializer(datetime_format, deep)
            if '_state' in attr_list:
                attr_list.pop('_state')
            if include_attr is not None:
                new_attr_list = {}
                for i in include_attr:
                    try:
                        new_attr_list[i] = attr_list[i]
                    except Exception, e:
                        print 'no include attr' + str(e)
                        continue
                attr_list = new_attr_list
            # datetime_list = [i for i in attr_list.items() if isinstance(i[1], datetime.datetime)]
            # if len(datetime_list) > 0:
            #     for i in datetime_list:
            #         attr_list[i[0]] = time_format_func(i[1])
            if except_attr is not None:
                for i in except_attr:
                    try:
                        attr_list.pop(i)
                    except Exception, e:
                        print 'no except attr' + str(e)
                        continue
            if isinstance(djmodels, list):
                result = attr_list
                break
            else:
                result.append(copy.copy(attr_list))
    if serializer == 'json':
        return simplejson.dumps(result)
    elif serializer == 'dict':
        return result
    elif serializer == 'xml':
        dd = {'xmlobj': result}
        return xmltodict.unparse(dd)
    return None



def create_verify_code():
    new_verify = create_random_str()
    image = Image.new('RGB', (147, 49), color=(255, 255, 255))  # model, size, background color
    font_file = os.path.join(BASE, 'static/blog/fonts/lato/lato-black.ttf')  # choose a font file
    font = ImageFont.truetype(font_file, 47)  # the font object
    draw = ImageDraw.Draw(image)
    draw.text((7, 0), new_verify, fill=(0, 0, 0), font=font)  # position, content, color, font
    del draw
    # request.session['captcha'] = rand_str.lower()
    img_name = 'ver' + str(time.time()).split('.')[0] + '.png'
    img_path = BASE + '/static/blog/img/verify/' + img_name
    image.save(img_path, 'png')
    return img_name, new_verify
