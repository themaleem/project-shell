from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    bio= models.TextField(blank=True)
    # posts=models.ManyToManyField(to='Post')
    joined=models.DateField(auto_now=True)

    def __str__(self):
        return "{}/s profile".format(self.user.username)


@receiver(post_save,sender=User)
def user_is_created(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
  else:
    instance.profile.save()