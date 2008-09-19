from django.shortcuts import render_to_response
from django.http import HttpResponse
from dojango.decorators import json_response
from models import Post

@json_response
def post(request):
    msg = request.POST['text']
    Post.objects.create(user=request.user, message=msg)
    lasts = Post.objects.filter(user__groups__in=request.user.groups.all()).order_by('-date').distinct()
    lasts = list(lasts[:10])
    lasts.reverse()
    messages = ''
    for m in lasts:
        messages += 'from %s:%s<br>' % (request.user.username, m.message)
    return {'success':True, 'messages':messages}

def testpost(request):
    lasts = Post.objects.filter(user__groups__in=request.user.groups.all()).order_by('-date').distinct()
    lasts = list(lasts[:10])
    lasts.reverse()
    messages = ''
    for m in lasts:
        messages += 'from %s:%s<br>' % (request.user.username, m.message)
    return HttpResponse(messages)