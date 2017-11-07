from django.shortcuts import render, redirect
import random
from django.db import transaction
from .models import Room
from django.core.urlresolvers import resolve
from django.contrib.auth.decorators import login_required
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
  print("This better work" + label)
  return render(request,"room.html",{
    'room':room,
    'messages':messages,
    'user':user,
    })

