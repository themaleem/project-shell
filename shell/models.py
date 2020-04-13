from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    posts = models.ManyToManyField(to='Post')
    joined = models.DateField(auto_now=True)

    def __str__(self):
        return "{}/s profile".format(self.user.username)

    class Meta:
        verbose_name="Profile"

@receiver(post_save,sender=User)
def user_is_created(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
  else:
    instance.profile.save()

class Postable(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    class Meta:
        abstract=True

class Post(Postable):
    
    def __str__(self):
        return f'{self.title[:10]}'
    
class Draft(Postable):
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title[:10]}'
        
class Response(models.Model):
    body = models.TextField()
    post = models.ForeignKey(to="Post",on_delete=models.CASCADE, related_name="responses")