from channels import Group
from channels.sessions import channel_session
from .models import *
import logging
import json
log = logging.getLogger(__name__)
@channel_session
def ws_connect(message):
  #prefix, label = message['path'].strip('/').split('/')
  #print(label)
  pre,pre,label = message['path'].strip('/').split('/') 
  print(label)
  room = Room.objects.get(label=label)
  Group('chat-' + label).add(message.reply_channel)
  message.channel_session['room'] = room.label
  message.reply_channel.send({'accept':True})
#  ws_receive(message)
@channel_session
def ws_receive(message):
  label = message.channel_session['room']
  room = Room.objects.get(label=label)
  print("receiving...")
  data = json.loads(message['text'])
  m = room.messages.create(handle=data['handle'],message=data['message'])
  Group('chat-'+label).send({'text':json.dumps(m.as_dict())})

@channel_session
def ws_disconnect(message):
  label = message.channel_session['room']
  room = Room.objects.get(label=label)
  room_users = chat_users.objects.filter(room=room).values_list('user_name',flat=True)
  Room_users = list(room_users)
  num_users = len(Room_users)
  if num_users < 1:
    room.delete()
  Group('chat-'+label).discard(message.reply_channel)
