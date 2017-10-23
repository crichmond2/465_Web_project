from django import forms
from django.core.validators import validate_unicode_slug
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm

class Registration_form(UserCreationForm):
  email = forms.EmailField(widget = forms.TextInput(attrs={'placeholder':'example@example.com'}),
                           required = True)
  firstname = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'First Name'}),
                              required = True)
  lastname = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Last Name'}),
                             required = True)
  username = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Username'}),
                             required = True)
  password1 = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Password'}),
                              required = True)
  password2 = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Re-type Password'}),
                              required = True)
  class Meta:
    model = User
    fields = ("username","firstname","lastname","email",
              "password1","password2")

  def save(self,commit=True):
    user=super(Registration_form,self).save(commit=False)
    user.email=self.cleaned_data["email"]
    user.firstname = self.cleaned_data["firstname"]
    user.lastname = self.cleaned_data["lastname"]
    if commit:
      user.save()
    return user

