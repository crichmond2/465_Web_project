from django.shortcuts import render, redirect
import random
from django.db import transaction
from .models import *
from django.core.urlresolvers import resolve,reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponseRedirect
import datetime
# Create your views here.
@login_required
def new_room(request,label):
  new_room = None
#  while not new_room:
  with transaction.atomic():
    label = label 
    if Room.objects.filter(label=label).exists():
      return chat_room(request,label)#      continue
    new_room = Room.objects.create(label = label)
  print("should redirect")
  return redirect(chat_room,label) 
@login_required
def chat_room(request,label):#,label):
  room, created = Room.objects.get_or_create(label=label) #get_or_create
  messages = reversed(room.messages.order_by('-timestamp')[:50])
  user = request.user.get_username()
  User = str(user)
  data = {'room':room,'username':user}
  Registered = chat_users.objects.all().filter(room=room).values_list('user_name',flat=True)
  #Registered = chat_users.objects.all().filter(room=room).values_list(user
  register = list(Registered)
  print(len(register))
  print(register)
  #Register = Registered.filter(user_name = user)
  
  registered = False
  if user in register:
    registered = True
  
  if request.method == 'POST':
    if(registered == False):
      form = chat_register(request.POST)
      form = chat_register(data) 
      if form.is_valid():
        form.save(commit=True)
    if(registered == True):
      user = chat_users.objects.filter(user_name=user).delete()
    return HttpResponseRedirect('/chat/'+label)
    request.session.modified = True
  print(registered)
      #return HttpResponseRedirect("")
#    if(registered == True):
      #request.session.modified = True
      #form.delete()
  form = chat_register(data) 
  form.fields["username"].widget = forms.HiddenInput()
  form.fields["room"].widget = forms.HiddenInput()
  #print("This better work" + label)
  return render(request,"room.html",{
    'room':room,
    'messages':messages,
    'user':user,
    'register':form,
    'registered':registered,
    'room_users':register,
    })


