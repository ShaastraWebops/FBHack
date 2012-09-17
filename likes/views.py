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
    users = FBUserProfile.objects.all().order_by('likes_used')[:likes]
    cnt = 0
    for user in users :
      cnt = cnt +1
      #response = urllib.urlopen('https://graph.facebook.com/' + post.post_id + '/likes?access_token='+ user.access_token).read()
      #if response == 'true' :
	#cnt = cnt + 1
	# user.likes_used = user.likes_used + 1
	# user.save()
    # post.likes_given = post.likes_given + cnt
    # post.save()
    assert False
    return HttpResponseRedirect(settings.SITE_URL)  
  return Http404()
