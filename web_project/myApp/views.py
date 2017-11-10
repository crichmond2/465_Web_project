from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.urls import resolve
from django.views.generic.detail import DetailView
from pusherable.mixins import PusherDetailMixin
from .models import *
from .forms import *
import random
import os
# Create your views here.
def login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request,username=username,password=password)
  if user is not None:
    login(request,user)
#    redirection = "/accounts/profile/" + username
#    print(redirection)
#    return redirect("/accounts/profile/RLChris")
  #if request.method == 'POST':
  #  form = Login_form(request.POST)
  #  if form.is_valid():
  #    form.save(commit=True)
  #    return redirect("/")
  #else:
  #  form = Login_form()
  #context={'form':form}
  #return render(request,"login.html",context)
def add_school(request):
  return render(request,"add_school.html")
def register(request):
  if request.method == 'POST':
    form = Registration_form(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return redirect("/")
  else:
    form = Registration_form()
  context = {"form":form}
  print("didn't work")
  return render(request,"register2.html",context)
def index(request):
  text = User.objects.all()
  return render(request,"content.html",locals())

def logout_(request):
  logout(request)
  return redirect("/")
@login_required
def profile(request,USER):
  form = Extended_user_form()
  full_name = request.user.get_full_name()
  prof = ((request.get_full_path()).split('/profile/')[1]).split('/')[0]
  user = request.user.get_username()
  prof_first_name = User.objects.all().filter(username=prof).values_list('first_name',flat=True)
  first_name = list(prof_first_name)
  prof_last_name = User.objects.all().filter(username=prof).values_list('last_name',flat=True)
  last_name = list(prof_last_name)
  rand_num = random.randint(0,1000000)
  chat_link = "chat/new_P"+str(rand_num)+((first_name[0])[0])
  if user == prof:
    owner = True
  else:
    owner = False
  context = {"form":form, 
             "name":full_name,
             "owner":owner,
             "prof_first_name":first_name[0],
             "prof_last_name":last_name[0],
             "chat_link":chat_link,
            }
  return render(request,"profile.html",context)

def login_redir(request):
  user = request.user.get_username()
  redirection = 'accounts/profile/%s/' % user
  return HttpResponseRedirect(redirection)
 # def get_context_data(self,**kwargs):
  #  context = super(ArticleDetailView, self).get_context_data(**kwargs)
    
#@login_required
#def chat_room(request,label):
#	#If the room with the given label doesn't exist, create a new one 
#	room,created = Room.objects.get_or_create(label=label)
	#show last 50 messages
#	messages = reversed(room.messages.order_by('-timstamp')[:50])
#	return render(request, "chat_room.html", {'room':room,'messages:messages'})

