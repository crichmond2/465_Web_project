from django.shortcuts import render, redirect
import random
from django.db import transaction
from .models import Room
from django.core.urlresolvers import resolve
# Create your views here.
def new_room(request):
  new_room = None
#  while not new_room:
  with transaction.atomic():
    label = "testing"
    if Room.objects.filter(label=label).exists():
      return chat_room(request,label)#      continue
    new_room = Room.objects.create(label = label)
  print("should redirect")
  return redirect(chat_room) 
def chat_room(request,label):#,label):
  room, created = Room.objects.get_or_create(label=label)
  messages = reversed(room.messages.order_by('-timestamp')[:50])
  print(room)
  print(created)
  return render(request,"room.html",{
    'room':room,
    'messages':messages,
    })
