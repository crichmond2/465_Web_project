from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import FormView
from .models import *
from .forms import *
# Create your views here.
def login(request):
  if request.method == 'POST':
    form = Login_form(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return redirect("/")
  else:
    form = Login_form()
  context={'form':form}
  return render(request,"login.html",context)
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
  return render(request,"register.html",context)
def index(request):
  text = User.objects.all()
  return render(request,"content.html",locals())



def profile(request):
  form = Extended_user_form()
  context = {"form":form}
  return render(request,"profile.html",context)
