from django.db import models
from django.utils import timezone
SCHOOL_LIST =(
    ('CSUC','Chico State'),
    ('CSUCI','Cal State Channel Islands'),
    ('UCLA','UCLA'),
)
#class User(models.Model):
#  FirstName = models.CharField(max_length=40)

#  LastName = models.CharField(max_length=40)
#  school = models.CharField(max_length=3,choices=SCHOOL_LIST)
#  email = models.EmailField(max_length=100)

  #def __str__(self):
  #  return_list = {FirstName,LastName}
  #  return return_list
#  profile_image = models.ImageField(upload_to='media/user_pics/')
#  def __str__(self):
 #   return_list = {FirstName,LastName}
#    return self.objects.all()

# Create your models here.
class Extended_user(models.Model):
  school = models.CharField(max_length=200)
  user = models.CharField(max_length=100,default='null')  
  def save(self,commit=True,*args,**kwargs):
    if(commit==True):
      super(Extended_user,self).save(*args,**kwargs)
  #years = models.IntegerField()
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date_published')
class Choice(models.Model):
  question = models.ForeignKey(Question)
  choice_text = models.CharField(max_length = 200)
  votes = models.IntegerField(default=0)
class Schools(models.Model):
  School = models.CharField(max_length=100)
  def __str__(self):
    return self.School
  def save(self,commit = True ,*args,**kwargs):
    if(commit == True):
      super(Schools,self).save(*args,**kwargs)
class Post(models.Model):
  Title = models.CharField(default = "",max_length=100)
  Post = models.TextField()
  user = models.CharField(max_length=100)
  def save(self,commit = True,*args,**kwargs):
    if(commit==True):
      super(Post,self).save(*args,**kwargs)
class Comment(models.Model):
  post = models.ForeignKey(Post,default="1",on_delete=models.CASCADE,related_name = "comment")
  user = models.CharField(max_length=100)
  comment = models.CharField(max_length=400)
  timestamp = models.DateTimeField(default=timezone.now,db_index=True)
  def as_dict(self):
    return {'user':self.handle, 'comment':self.message,'timestamp':self.timestamp}
  def formatted_timestamp(self):
    return self.timestamp.strftime('%b %-d %-I:%M %p')
  def save(self,*args,**kwargs):
    super(Comment,self).save(*args,**kwargs)

#class Room(models.Model):
#	name = models.TextField()
#	label = models.SlugField(unique=True)

#class Message(models.Model):
#	room = models.ForeignKey(Room,related_name="messages")
#	handle = models.TextField()
#	message = models.TextField()
#	timestamp = models.DateTimeField(default=timezone.now,db_index=True)

