from django import forms
from .models import *
class chat_register(forms.Form):
  room = forms.CharField(label = "room",max_length = 200, required = True)
  username = forms.CharField(label = "username",max_length = 200,required = True)
  class Meta:
    model = chat_users()
    fields =("username","room")
  def save(self,commit=True):
    user = chat_users()
    user.room = self.cleaned_data["room"]
    user.user_name = self.cleaned_data["username"]
    if commit:
      user.save()
    return user

