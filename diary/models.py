from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Diary(models.Model):
  title = models.CharField(max_length=500)
  user = models.ForeignKey(User)

  class Meta:
      verbose_name = 'Diary'
      verbose_name_plural = 'Diaries'

  def __str__(self):
      return '{} added a Diary {}'.format(self.user.username,self.title)
