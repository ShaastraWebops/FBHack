from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from users.forms import *
from users.models import *
from FBHack.likes.models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import urllib, json
from django.conf import settings

def home(request):
  if request.user.is_authenticated():
    users = FBUserProfile.objects.all()
    posts=[]
    '''
    target = urllib.urlopen('https://graph.facebook.com/Shaastra/posts?limit=50&access_token='+ settings.FACEBOOK_APP_ACCESS_TOKEN).read()
    response = json.loads(target)    
    data = response['data']
    for p in data:
      if p['type'] == 'status' or p['type'] == 'question' :
	continue
      post_id = p['id']
      try:
	desc = p['message']
      except:
	desc = p['story']
      likes = p['likes']['count']
      try:
	shares = p['shares']['count']
      except:
	shares = 0
      link = p.get('link',"")
      try:
	old_post = FBPosts.objects.get(post_id=p['id'])
	old_post.likes = likes
	old_post.shares = shares
	old_post.save()
	continue
      except:
	new_post = FBPosts(desc=desc, post_id = post_id, likes=likes, shares=shares, link = link)
	new_post.save()
	posts.append(new_post)
    '''
    posts.extend(FBPosts.objects.all())
    add_form = AddForm()
   # assert False
    return render_to_response('users/home.html', locals(), context_instance=RequestContext(request))  
  return HttpResponseRedirect('/login')

def login(request):
  if request.method=="POST":
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth_login(request, user)
	return HttpResponseRedirect('/')
    msg = 'Invalid Username or Password.'
    login_form = LoginForm()
    return render_to_response('users/login.html', locals(), context_instance=RequestContext(request))
  login_form = LoginForm()
  return render_to_response('users/login.html', locals(), context_instance=RequestContext(request))

def register(request):
  return HttpResponse("Register")

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')