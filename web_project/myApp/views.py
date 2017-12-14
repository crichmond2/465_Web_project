from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import resolve
from django.views.generic.detail import DetailView
from pusherable.mixins import PusherDetailMixin
from .models import *
from chat.models import chat_users, Room
from .forms import *
import random
import os
import datetime
# Create your views here.
now = datetime.datetime.now()
def home(request):
    if(request.method == 'POST'):
      form = Search_form(request.POST)
      school_results = list()
      post_results = list()
      chat_results = list()
      post_titles = list()
      chat_rooms = Room.objects.all().values_list()
      schools = Schools.objects.all().values_list()
      posts = Post.objects.all().values_list()
      if(form.is_valid()):
        search = form.get()
        print(search)
        for i,j,x in chat_rooms:
          if(search in x):
            chat_results.append(x)
        for i,x in schools:
          #print(x)
          #print(search)
          if(search in x or search == x):
           # print(i + "," + x)
            school_results.append(x)
        for a,i,x,j in posts:
          if(search in x):
            post_results.append(x)
            post_titles.append(i)
          #print(x)
        #print(results)
        form = Search_form()
        context = {"school_results":school_results,"chat_results":chat_results,"post_titles":post_titles,"post_results":post_results,"search":search}
        #return redirect("results",context)
        return results(request,context,search)
        #return render(request,"results.html",context)
    if(request.user.is_authenticated()):
      User = request.user.username
    else:
      User = "empty"
    form = Search_form()
    context = {"form":form,'User':User}
    return render(request,"homepage.html",context)
#@login_required
def post_history(request):
  Title = Post.objects.all().filter(user=request.user.get_username()).values_list('Title',flat=True)
  post = Post.objects.all().filter(user=request.user.get_username()).values_list('Post',flat=True)
  post_list = list(post)
  title_list = list(Title)
  title_list2 = list()
  for x in title_list:
    title_list2.append(x)
  post_list2 = list()
  for x in post_list:
    post_list2.append(x.split("["))
  posts = {'Title':title_list2}
  #Title = list(title)
  #post = list(Post)
  #print(post)
  #print(Title)
  context = {'posts':Title}
  return render(request,"post_history.html",context)
def posting(request,title):
  if(request.method=='POST'):
    TiTles = Post.objects.get(Title = title)
    form = comment_form(request.POST)
    if form.is_valid():
      com = Comment()
      com.Post = TiTles.id
      com.user = request.user.get_username()
      com.comment = form.cleaned_data['comment']
      com.timestamp = now.isoformat()
      com.save()
  titles = Post.objects.all().filter(Title = title).values_list('Title',flat=True)
  Posts = Post.objects.all().filter(Title=title).values_list('Post',flat=True)
  Titles = list(titles)
  TiTles = Post.objects.get(Title = title)
  posts = list(Posts)
  form = comment_form()
  messages = reversed(TiTles.comment.order_by('-timestamp')[:10])
  context = {'posts':posts,'Titles':Titles,'comment':messages,'form':form}
  return render(request,"postings.html",context)
def login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request,username=username,password=password)
  if user is not None:
    login(request,user)
#    redirection = "/accounts/profile/" + username
#    print(redirection)
#    return redirect("/accounts/profile/RLChris")
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
  if request.method == 'POST':
    form = AddSchool(request.POST)
    if form.is_valid():
      print(form.cleaned_data["school"])
      data = {"school":form.cleaned_data["school"]}
      form = AddSchool(data)
      if(form.is_valid()):
        form.save()
      return redirect("/")
  form = AddSchool()
  context = {'form':form}
  return render(request,"add_school.html",context)
def register(request):
  if request.method == 'POST':
    form = Registration_form(request.POST)
    #form2 = Schools(request.POST) 
    if form.is_valid():
      data = {'school':form.cleaned_data['school'],'user': form.cleaned_data['username']}
      ext_u = Extended_user()
      ext_u.school = form.cleaned_data['school']
      ext_u.user = form.cleaned_data['username']
      ext_u.save(commit=True)
      form.save(commit=True)
    #if form2.is_valid():
    #form = Extended_user(data)
    #  if(form.is_valid()):
    #form.save(commit=True)
      return redirect("/")
  else:
    form = Registration_form()
  context = {"form":form}
  print("didn't work")
  return render(request,"register2.html",context)
def filters(request):
  if request.method == "POST":
    form = request.POST.getlist('filter')
    form2 = Search_form(request.POST)
    if(form2.is_valid()):
      search = form2.get()
    #print(form)
    #print(search)
    chat_results = list()
    post_results = list()
    post_titles = list()
    school_results = list()
    people_results = list()
    chat_rooms = Room.objects.all().values_list()
    posts = Post.objects.all().values_list()
    schools = Schools.objects.all().values_list()
    users = User.objects.all().values_list('username',flat=True)
    if("Chats" in form):
      for i,j,x in chat_rooms:
        if(search in x):
          chat_results.append(x)
    if("Schools" in form):
      for i,x in schools:
        if(search in x):
          school_results.append(x)
    if("Posts" in form):
      for a,i,x,j in posts:
        if(search in x):
          post_results.append(x)
          post_titles.append(i)
    if("People" in form):
      for x in users:
        if(search in x):
          people_results.append(x)
          
    data = {"search_field":search}
    form2 = Search_form(data)
    context = {"school_results":school_results,"people_results":people_results,"chat_results":chat_results,"post_titles":post_titles,"post_results":post_results,"form2":form2}
    return render(request,"results.html",context)
  return redirect('/')
def index(request):
  text = User.objects.all()
  return render(request,"content.html",locals())
def results(request,context,search):
  form = filter_form()
  data = {"search_field":search}
  form2 = Search_form(data)
  context["form"] = form
  context["form2"] = form2
  return render(request,"results.html",context)
def logout_(request):
  logout(request)
  return redirect("/")
@login_required
def post(request):
  if(request.method=="POST"):
    form = post_form(request.POST)
    print(form.is_valid())
    if(form.is_valid()):
      User,Text,Title = form.get()
      print(Title + " "+ User + " " + Text)
      data = {'user':User,'text':Text} 
      post = Post()
      post.user = User
      post.text = Text
      post.Title = Title
      #post.save()
      instance = form.save(commit=False)
      instance.user = User
      instance.Post = Text
      instance.Title = Title
      instance.save()
      return redirect('/')
  data = {'user':request.user.username}
  form = post_form(data) 
  context = {'form':form}
  return render(request,"post.html",context)
@login_required
def profile(request,USER):
  form = Extended_user_form()
  full_name = request.user.get_full_name()
  prof = ((request.get_full_path()).split('/profile/')[1]).split('/')[0]
  user = request.user.get_username()
  prof_first_name = User.objects.all().filter(username=prof).values_list('first_name',flat=True)
  first_name = list(prof_first_name)
  prof_last_name = User.objects.all().filter(username=prof).values_list('last_name',flat=True)
  chatRooms = chat_users.objects.all().filter(user_name=user).values_list('room',flat=True)
  posts = Post.objects.all().filter(user=user).values_list('Post',flat=True)
  Email = User.objects.all().filter(username=prof).values_list('email',flat=True)
  School = Extended_user.objects.all().filter(user=prof).values_list('school',flat=True)
  school = list(School)
  room_list = list(chatRooms)
  email = list(Email)
  last_name = list(prof_last_name)
  print(len(room_list))
  print(room_list)
  print(user)
  rand_num = random.randint(0,1000000)
  chat_link = "chat/new_P"+str(rand_num)+((first_name[0])[0])
  if user == prof:
    owner = True
  else:
    owner = False
  context = {"form":form,
             "name":full_name,
             "owner":owner,
             "prof_first_name":first_name[0],
             "prof_last_name":last_name[0],
             "chat_link":chat_link,
             "chat_rooms":room_list,
             "posts":posts,
             "email":email,
             "school":school,
            }
  return render(request,"profile.html",context)
def django(request):
  return render(request,"django.html")
def login_redir(request):
  user = request.user.get_username()
  redirection = 'accounts/profile/%s/' % user
  return HttpResponseRedirect(redirection)
 # def get_context_data(self,**kwargs):
  #  context = super(ArticleDetailView, self).get_context_data(**kwargs)

#@login_required
#def chat_room(request,label):
#	#If the room with the given label doesn't exist, create a new one
#	room,created = Room.objects.get_or_create(label=label)
	#show last 50 messages
#	messages = reversed(room.messages.order_by('-timstamp')[:50])
#	return render(request, "chat_room.html", {'room':room,'messages:messages'})
