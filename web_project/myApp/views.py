from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
# Create your views here.

def register(request):
  if request.method == 'POST':
    form = Registration_form(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return redirect("/")
  else:
    form = Registration_form()
  context = {"form":form}
  return render(request,"register.html",context)

def index(request):
  text = User.objects.all()
  return render(request,"content.html",locals())
