from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
import urllib, json
from django.conf import settings
from FBHack.likes.models import *

def likes(request):
  if request.method=="POST" :
    likes = request.POST.get("likes",0)
    shares = request.POST.get("shares",0)
    pid = request.POST.get("pid",0)
    post = FBPosts.objects.get(id=pid)
    users = FBUserProfile.objects.all()
    for user in users :
      response = urllib.urlopen('https://graph.facebook.com/' + post.post_id + '/likes?access_token='+ user.access_token).read()
      if response == 'true' :
	likes=likes-1
      if likes :
	break
    return HttpResponseRedirect(settings.SITE_URL)  
  return Http404()
