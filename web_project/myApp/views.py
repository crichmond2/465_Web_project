from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import FormView
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from pusherable.mixins import PusherDetailMixin
from .models import *
from .forms import *
# Create your views here.
def login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request,username=username,password=password)
  if user is not None:
    login(request,user)
    return redirect("/accounts/profile")
  #if request.method == 'POST':
  #  form = Login_form(request.POST)
  #  if form.is_valid():
  #    form.save(commit=True)
  #    return redirect("/")
  #else:
  #  form = Login_form()
  #context={'form':form}
  #return render(request,"login.html",context)
def add_school(request):
  return render(request,"add_school.html")
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
  return render(request,"register2.html",context)
def index(request):
  text = User.objects.all()
  return render(request,"content.html",locals())

def logout_(request):
  logout(request)
  return redirect("/")
@login_required
def profile(request):
  form = Extended_user_form()
  full_name = request.user.get_full_name()
  context = {"form":form, "name":full_name}
  return render(request,"profile.html",context)

def popup(request):
  return render(request,"color_form.html")
class ColorFormView(FormView):
  template_name='color_form.html'
  form_class = ColorForm
  def form_valid(self,form):
    color = form.cleaned_data.get("color")
    return HttpResponse("Your color:{0}".format(color))
class PusherableExampleDetail(PusherDetailMixin,DetailView):
  model = PusherableExample
  template_name = "example.html"
#@login_required
#def chat_room(request,label):
#	#If the room with the given label doesn't exist, create a new one 
#	room,created = Room.objects.get_or_create(label=label)
	#show last 50 messages
#	messages = reversed(room.messages.order_by('-timstamp')[:50])
#	return render(request, "chat_room.html", {'room':room,'messages:messages'})

