from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import string,random

# function to generate a random value
def generate_username(size=7, chars=string.ascii_uppercase + string.digits):
    return 'user'+''.join(random.choice(chars) for _ in range(size))
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    generated_username = models.CharField(max_length=20)
    status = models.TextField(max_length=100, null=True, blank=True, default="Love and Light!")
    avatar = models.ImageField(upload_to='avis/',blank=True)
    one_word_description = models.CharField(max_length=15)
    bio = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def save(self, *args, **kwargs):
        self.generated_username = generate_username()
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username



@receiver(post_save,sender=User)
def user_is_created(sender, instance ,created ,**kwargs):
  if created:
    Profile.objects.create(user=instance)
  else:
    instance.profile.save()
