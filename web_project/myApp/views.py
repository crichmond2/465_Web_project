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
import os
# Create your views here.
def login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request,username=username,password=password)
  if user is not None:
    login(request,user)
    redirection = "/accounts/profile/" + username
    print(redirection)
    return redirect("/accounts/profile/RLChris")
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
  print(prof)
  print(user)
  if user == prof:
    owner = True
  else:
    owner = False
  context = {"form":form, "name":full_name,"owner":owner}
  return render(request,"profile.html",context)

def popup(request):
  return render(request,"color_form.html")
class ColorFormView(FormView):
  template_name='color_form.html'
  form_class = ColorForm
  def form_valid(self,form):
    color = form.cleaned_data.get("color")
    return HttpResponse("Your color:{0}".format(color))
class PusherableExampleDetail(PusherDetailMixin,DetailView):
  model = PusherableExample
  template_name = "example.html"
def login_redir(request):
  user = request.user.get_username()
  redirection = 'accounts/profile/%s/' % user
  return HttpResponseRedirect(redirection)
#@login_required
#def chat_room(request,label):
#	#If the room with the given label doesn't exist, create a new one 
#	room,created = Room.objects.get_or_create(label=label)
	#show last 50 messages
#	messages = reversed(room.messages.order_by('-timstamp')[:50])
#	return render(request, "chat_room.html", {'room':room,'messages:messages'})

