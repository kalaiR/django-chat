from django.shortcuts import render_to_response
from django.http import HttpResponse
from dojango.decorators import json_response
from models import Post
from models import UserData
from datetime import datetime, timedelta
from django.conf import settings

@json_response
def post(request):
    msg = request.POST['text']
    Post.objects.create(user=request.user, message=msg)
    return get_posts(request)

def testpost(request):
    messages = get_posts(request)['messages']
    return HttpResponse(messages)

def get_posts(request):
    now = datetime.now()
    udata, created = UserData.objects.get_or_create(user=request.user)
    udata.last_req = now
    if not udata.connected:
        udata.connected = True
        admin = User.objects.get(username=settings.ADMINS[0][0])
        Post.objects.create(user=admin, message='%s is connected.' % request.user.username)
    udata.save()
    
    # users connected
    before = now - timedelta(seconds=settings.CONNECTED_AFTER_LAST_REQ)
    userlist = []
    for ud in UserData.objects.all():
        if ud.last_req > before:
            userlist.append(ud.user.username)
        else:
            if udata.connected:
                udata.connected = False
                udata.save()
    
    lasts = Post.objects.filter(user__groups__in=request.user.groups.all()).order_by('-date').distinct()
    lasts = list(lasts[:10])
    lasts.reverse()
    messages = ''
    for m in lasts:
        messages += 'from %s:%s<br>' % (m.user.username, m.message)
    return {'success':True, 'messages':messages, 'users':userlist}