from django import forms
from django.core.validators import validate_unicode_slug
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from .models import *
SCHOOL_LIST =(
    ('CSUC','Chico State'),
    ('CSUCI','Cal State Channel Islands'),
    ('UCLA','UCLA'),
)
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
  school = forms.ChoiceField(choices=SCHOOL_LIST,required=True)
  class Meta:
    model = User
    fields = ("username","firstname","lastname","email",
              "password1","password2","school")

  def save(self,commit=True):
    user=super(Registration_form,self).save(commit=False)
    user.email=self.cleaned_data["email"]
    user.first_name = self.cleaned_data["firstname"]
    user.last_name = self.cleaned_data["lastname"]
    user.school = self.cleaned_data["school"]
    if commit:
      user.save()
    return user

class Extended_user_form(forms.Form):
  school = forms.CharField(label = "School",max_length = 100,required = True)
  years = forms.CharField(label = "Years", max_length = 100)
  class Meta:
    model = Extended_user
    fields = ('School','years')


class Login_form(AuthenticationForm):
  username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}),
                          max_length=40,
                          validators=[validate_unicode_slug],
                          label="Username"
                          )
  password=forms.CharField(label = "Password",
                           max_length=40,
                           widget=forms.PasswordInput(),
                           )
 
#class school_form(forms.ModelForm):
#  class Meta:
#    model = school
#  def save(self,commit=True):
#    user-
