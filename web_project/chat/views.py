from django.shortcuts import render

# Create your views here.
def chat_room(request,label):
  room, created = Room.objects.get_or_create(label=label)
  messages = reversed(room.messages.order_by('-timstamp')[:50])
  return render(request,"chat/room.html",{
    'room':room,
    'messages':messages,
    })
