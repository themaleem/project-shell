from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class FeedManager(models.Manager):
    def all_feeds(self):
        return super().get_queryset()

    def published(self):
        # this gives all the published feeds
        return super().get_queryset().filter(is_published=True)

    def draft(self):
        # this gives all the feeds that aren't published 
        return super().get_queryset().filter(is_published=False)

class Feed(models.Model):
    STATUS_CHOICES = (
        ('published','Published'),
        ('draft','Draft')
    )
    title = models.CharField(max_length=200)
    # We have added the unique_for_date parameter to this field so that we can build URLs for posts using
    # their publish date and slug . Django will prevent multiple posts from having the same slug for a given date
    slug = models.SlugField(unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_feeds',null=True,blank=True)
    body = models.TextField()
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='draft',choices=STATUS_CHOICES,max_length=10)
    tags = TaggableManager()

    objects = FeedManager()

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Feed,self).save(*args,**kwargs)


    def comments_count(self):
        return self.comments.filter(active=True).count()

    class Meta:
        verbose_name = 'Feed'
        verbose_name_plural = 'Feeds'
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    feed = models.ForeignKey(Feed,related_name='comments',on_delete=models.CASCADE)
    comment_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default =True)
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'



    def __str__(self):
        return '{} added a comment on {}'.format(self.creator,self.feed)

class Diary(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='diaries')
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Diary'
        verbose_name_plural = 'Diaries'

    def __str__(self):
        return f'{self.title.upper()} by {self.owner.username}'
