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


class Proxy(BaseModel):
    ip = models.CharField(max_length=30, unique=True)
    online = models.BooleanField(default=True)

    def __unicode__(self):
        return self.ip


class ProxyUser(BaseModel):
    token = models.CharField(max_length=64)
    ip = models.CharField(max_length=20)
    record = models.CharField(max_length=1000, default='')

    def __unicode__(self):
        return self.token