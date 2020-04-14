from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    generated_username = models.CharField(max_length=20)
    followers = models.ManyToManyField(User, related_name="followers_profile", blank=True)

    following = models.ManyToManyField(User, related_name="following_profile", blank=True)

    status = models.TextField(max_length=100, null=True, blank=True, default="Yeah! I am at HUSKY!")
    avatar = models.ImageField(upload_to='')
    one_word_description = models.CharField(max_length=15)
    bio = models.TextField()

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    def __str__(self):
        return self.user.username



@receiver(post_save,sender=User)
def user_is_created(sender, instance ,created ,**kwargs):
  if created:
    Profile.objects.create(user=instance)
  else:
    instance.profile.save()
