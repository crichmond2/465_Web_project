from django.db.models.signals import pre_save,pre_delete,post_save,post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Question, Choice
import os.path

@receiver(pre_delete,sender=Question)
@receiver(pre_delete,sender=Choice)
@receiver(pre_save,sender=Question)
@receiver(pre_save,sender=Choice)
def model_pre_change(sender, **kwargs):
  if os.path.isfile(settings.READ_ONLY_FILE):
    raise ReadOnlyException('Model is read only mode')
@receiver(post_save,sender=Question)
@receiver(post_save,sender=Choice)
def model_post_save(sender,**kwargs):
  print('Saved: {}'.format(kwargs['instance'].__dict__))

@receiver(post_delete,sender=Question)
@receiver(post_delete,sender=Choice)
def model_post_delete(sender,**kwargs):
  print('Delete: {}'.format(kwargs['instance'].__dict__))

class ReadOnlyException(Exception):
  pass
