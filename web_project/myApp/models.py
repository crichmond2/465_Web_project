from django.db import models

class User(models.Model):
  FirstName = models.CharField(max_length=40)
  LastName = models.CharField(max_length=40)
  #def __str__(self):
  #  return_list = {FirstName,LastName}
  #  return return_list
#  profile_image = models.ImageField(upload_to='media/user_pics/')
  def __str__(self):
 #   return_list = {FirstName,LastName}
    return self.User


# Create your models here.
