# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate

from app.utils import *
from app.myblog.models import *
from app.decorater import login_api
from app.decorater import login_require


# Create your views here.

def index(req):
    try:
        if req.session['user'] != '' or req.session['user'] is not None:
            return render_to_response("blog_admin.html")
    except:
        pass
    return render_to_response("badmin.html")


@login_require
def blog(req):
    return render_to_response("blog_admin.html")


@login_require
def know_admin(req):
    return render_to_response("know_admin.html")


@login_require
def comment_admin(req):
    return render_to_response("comment_admin.html")


@login_require
def know(req, kid=None):
    return render_to_response("new_know.html")


@login_require
def create_blog(req, bid=None):
    return render_to_response("new_blog.html")


@csrf_exempt
def login(req):
    body={}
    account = req.POST.get('account')
    password = req.POST.get('password')
    user = authenticate(username=account, password=password)
    if user is None:
        body['fail_mes'] = '用户或密码不正确～'
        return HttpResponse(encodejson(7, body), content_type="application/json")
    if not user.is_active:
        body['fail_mes'] = '用户已被禁用～'
        return HttpResponse(encodejson(13, body), content_type="application/json")
    req.session['user'] = account
    return HttpResponse(encodejson(1, body), content_type="application/json")


@csrf_exempt
@login_api
def new_blog(req):
    body={}
    caption = req.POST.get('caption')
    sub_caption = req.POST.get('sub_caption')
    classify = req.POST.get('classify')
    tag_str = str(req.POST.get('tags'))
    content = req.POST.get('content')
    bid = req.POST.get('id')
    pub = req.POST.get('publish')
    tag_str = tag_str.split(',')
    classifcation = Classification.objects.get(id=classify)
    if bid != '' and bid is not None:
        mblog = Article.objects.get(id=bid)
        mblog.caption = caption
        mblog.sub_caption = sub_caption
        mblog.content = content
        mblog.publish = pub
        mblog.classification = classifcation
        mblog.save()
    else:
        nblog = Article(caption=caption,
                           sub_caption=sub_caption,
                           content=content,
                           classification=classifcation,
                           publish=pub)
        nblog.save()
        for itm in tag_str:
            try:
                tag_list = Tag.objects.get(id=itm)
                nblog.tags.add(tag_list)
            except:
                continue
        nblog.save()
    return HttpResponse(encodejson(1, body), content_type='application/json')


@login_api
def get_blog_util(req, bid=None):
    body={}
    body['modify'] = False
    if bid is not None:
        blog = Article.objects.get(id=bid)
        blog_json = model_serializer(blog, deep=True)
        blog_json['tags'] = model_serializer(blog.tags, include_attr=['id', 'tag_name'])
        body['blog'] = blog_json
        body['modify'] = True
    classify = Classification.objects.all()
    classify_json = model_serializer(classify, include_attr=['id', 'c_name'])
    tags = Tag.objects.all()
    tags_json = model_serializer(tags, include_attr=['id', 'tag_name'])
    body['tags'] = tags_json
    body['classify'] = classify_json
    return HttpResponse(encodejson(1, body), content_type="application/json")


@login_api
def get_env(req, kid=None):
    body={}
    env_list = Env.objects.all()
    env_json = model_serializer(env_list, include_attr=['id', 'content'])
    if kid is not None:
        know = Knowledge.objects.get(id=kid)
        know_json = model_serializer(know, datetime_format="string")
        body['know'] = know_json
    body['env'] = env_json
    return HttpResponse(encodejson(1, body), content_type="application/json")


@csrf_exempt
@login_api
def new_tag(req):
    body={}
    try:
        tag = req.POST.get('tag')
        ntag = Tag(tag_name=tag)
        ntag.save()
        tag_list = Tag.objects.all()
        tag_json = model_serializer(tag_list, include_attr=['id', 'tag_name'])
        body['tags'] = tag_json
        body['type'] = 2
    except:
        body['fail_mes'] = 'Unknow Error'
        return HttpResponse(encodejson(2, body), content_type='application/json')
    return HttpResponse(encodejson(1, body), content_type="application/json")


@login_api
def new_classify(req):
    body={}
    try:
        classify = req.POST.get('classify')
        nclassify = Classification(c_name=classify)
        nclassify.save()
        classify_list = Classification.objects.all()
        classify_json = model_serializer(classify_list, include_attr=['id', 'c_name'])
        body['classify'] = classify_json
        body['type'] = 1
    except:
        body['fail_mes'] = 'Unknow Error'
        return HttpResponse(encodejson(2, body), content_type="application/json")
    return HttpResponse(encodejson(1, body), content_type='application/json')


@login_api
def new_env(req):
    body={}
    try:
        env = req.POST.get('env')
        nenv = Env(content=env)
        nenv.save()
        env_list = Env.objects.all()
        env_json = model_serializer(env_list, include_attr=['id', 'content'])
        body['env'] = env_json
    except:
        body['fail_mes'] = 'Unknow Error'
        return HttpResponse(encodejson(2, body), content_type="application/json")
    return HttpResponse(encodejson(1, body), content_type='application/json')


@csrf_exempt
@login_api
def new_know(req):
    body={}
    question = req.POST.get('question')
    answer = req.POST.get('answer')
    env_str = str(req.POST.get('env'))
    pub = req.POST.get('publish')
    kid = req.POST.get('id')
    if kid != '':
        mknow = Knowledge.objects.get(id=kid)
        mknow.question = question
        mknow.answer = answer
        mknow.publish = pub
        mknow.save()
    else:
        nknow = Knowledge(question=question,
                          answer=answer)
        nknow.save()
        env_str = env_str.split(',')
        for itm in env_str:
            try:
                senv = Env.objects.get(id=itm)
                nknow.env.add(senv)
            except:
                continue
        nknow.save()
    return HttpResponse(encodejson(1, body), content_type='application/json')


@login_api
def know_list(req):
    body={}
    knows = Knowledge.objects.all().order_by('-create_time')
    know_json = model_serializer(knows, datetime_format="string", except_attr=['answer'])
    # for i, itm in enumerate(knows):
    #     know_json[i]['env'] = model_serializer(itm.env.all(), include_attr=['content'])
    body['know_list'] = know_json
    return HttpResponse(encodejson(1, body), content_type='application/json')


@login_api
def blog_list(req):
    body={}
    blogs = Article.objects.all().order_by('-create_time')
    blog_json = model_serializer(blogs, datetime_format="string", except_attr=['content'])
    # for i, itm in enumerate(knows):
    #     know_json[i]['env'] = model_serializer(itm.env.all(), include_attr=['content'])
    body['blog_list'] = blog_json
    return HttpResponse(encodejson(1, body), content_type='application/json')


@login_api
def comment_list(req):
    body={}
    c_list = Comment.objects.all()
    comment_json = model_serializer(c_list, datetime_format="string")
    for i, itm in enumerate(c_list):
        comment_json[i]['belong'] = itm.belong.caption
        if comment_json[i]['reply']:
            comment_json[i]['reply_list'] = model_serializer(itm.replys.all(), datetime_format="string")
        else:
            comment_json[i]['reply_list'] = None
    body['comment_list'] = comment_json
    return HttpResponse(encodejson(1, body), content_type="application/json")


@csrf_exempt
@login_api
def blog_opt(req):
    body={}
    otype = int(req.POST.get("type"))
    bid = req.POST.get("bid")
    blog = Article.objects.get(id=str(bid))
    if otype == 1:
        blog_json = model_serializer(blog, datetime_format="string", deep=True)
        blog_json['tags'] = model_serializer(blog.tags, include_attr=['id', 'tag_name'])
        body['blog'] = blog_json
        return HttpResponse(encodejson(1, body), content_type="application/json")
    elif otype == 2:
        blog.delete()
        return HttpResponse(encodejson(1, body), content_type="application/json")
    elif otype == 3:
        blog.publish = not blog.publish
        blog.save()
        return HttpResponse(encodejson(1, body), content_type="application/json")
    else:
        pass
    return HttpResponse(encodejson(13, body), content_type="application/json")


@csrf_exempt
@login_api
def comment_opt_del(req):
    body={}
    otype = int(req.POST.get("type"))
    cid = req.POST.get("cid")
    if otype == 1:
        comment = Comment.objects.get(id=cid)
        blog = comment.belong
        blog.comment_count -= 1
        blog.save()
        if comment.reply:
            reply = comment.replys.all()
            for itm in reply:
                itm.delete()
        comment.delete()
    elif otype == 2:
        comment = CommentReply.objects.get(id=cid)
        blog = comment.replyed.belong
        blog.comment_count -= 1
        blog.save()
        comment.delete()
    return HttpResponse(encodejson(1, body), content_type="application/json")


@csrf_exempt
@login_api
def comment_opt_new(req):
    body={}
    otype = int(req.POST.get("type"))
    cid = req.POST.get("cid")
    to = req.POST.get('to')
    content = req.POST.get('content')
    # print '----'
    # print content
    new_reply = CommentReply(content=content,
                             author="RaPoSpectre",
                             avatar="master.png")
    if otype == 1:
        comment = Comment.objects.get(id=cid)
        comment.reply = True
        blog = comment.belong
        blog.comment_count += 1
        new_reply.replyed = comment
        new_reply.to = comment.author
        new_reply.save()
        comment.save()
        blog.save()
    elif otype == 2:
        r_comment = CommentReply.objects.get(id=to)
        comment = Comment.objects.get(id=cid)
        blog = comment.belong
        blog.comment_count += 1
        blog.save()
        new_reply.to = r_comment.author
        new_reply.replyed = comment
        new_reply.save()
    return HttpResponse(encodejson(1, body), content_type="application/json")


@csrf_exempt
@login_api
def know_opt(req):
    body={}
    otype = int(req.POST.get("type"))
    kid = req.POST.get("kid")
    know = Knowledge.objects.get(id=str(kid))
    if otype == 2:
        know.delete()
        return HttpResponse(encodejson(1, body), content_type="application/json")
    elif otype == 3:
        know.publish = not know.publish
        know.save()
        return HttpResponse(encodejson(1, body), content_type="application/json")
    else:
        pass
    return HttpResponse(encodejson(13, body), content_type="application/json")


def tt(req):
    return 0
