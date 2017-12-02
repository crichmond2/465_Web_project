from django import forms
from django.core.validators import validate_unicode_slug
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from .models import *
from django_popup_view_field.fields import PopupViewField
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
class AddSchool(forms.Form):
  school = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'School Name'}),label = "school",max_length = 100,required = True)
  class Meta:
    model = Schools
    fields=('school')
  def save(self,commit=True):
    school = Schools()
    school.school = self.cleaned_data['school']
    if(commit==True):
      school.save()
    return school
class Extended_user_form(forms.Form):
  school = forms.CharField(label = "School",max_length = 100,required = True)
  years = forms.CharField(label = "Years", max_length = 100)
  class Meta:
    model = Extended_user
    fields = ('School','years')
class post_form(forms.Form):
  user = forms.CharField(label="user",max_length = 100,required = True)
  text = forms.CharField(widget=forms.Textarea,label = 'text',required = True)
  class Meta:
    model = Post
    fields = ('user','text')
  def save(self,commit=True):
    model = Post()
    model.user=self.cleaned_data['user']
    model.text=self.cleaned_data['text']
    if(commit==True):
      model.save()
    return model
  def get(self):
    context = (self.cleaned_data['user'],self.cleaned_data['text'])
    return context
class Search_form(forms.Form):
  search_field = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Search..."}),label = "Search",max_length = 100,required = True)
  class Meta:
    fields = ('Search')
  def get(self):
    search = self.cleaned_data['search_field']
    return search
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
