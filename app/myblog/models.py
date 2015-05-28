# -*- coding: utf-8 -*-
import datetime

from django.db import models

from app.utils import datetime_to_string, datetime_to_timestamp, datetime_to_utc_string



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



class Classification(BaseModel):
    c_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.c_name


class Tag(BaseModel):
    tag_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.tag_name


class Article(BaseModel):
    caption = models.CharField(max_length=50)
    sub_caption = models.CharField(max_length=30, blank=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    # author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags_art', null=True)
    classification = models.ForeignKey(Classification, related_name='cls_art')
    content = models.TextField()
    publish = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Comment(BaseModel):
    content = models.TextField()
    author = models.CharField(max_length=100, default="匿名网友")
    avatar = models.CharField(max_length=300, default="default.png")
    reply = models.BooleanField(default=False)
    belong = models.ForeignKey(Article, related_name='comments')


    def __unicode__(self):
        return self.content


class CommentReply(BaseModel):
    content = models.TextField()
    author = models.CharField(max_length=100, default="匿名网友")
    avatar = models.CharField(max_length=300, default="default.png")
    replyed = models.ForeignKey(Comment, null=True, blank=True, related_name='replys')
    to = models.CharField(max_length=100, default='匿名网友')


    def __unicode__(self):
        return self.content


class Env(BaseModel):
    content = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.content


class Knowledge(BaseModel):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    publish = models.BooleanField(default=False)
    env = models.ManyToManyField(Env, related_name='knowledges', null=True, blank=True)

    def __unicode__(self):
        return self.question
