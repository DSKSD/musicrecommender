from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField(null=False)
    photo = ImageField(upload_to='%Y/%m/%d', null=True)
    artist = models.CharField(max_length=200)
    songname = models.CharField(max_length=200)
    videourl = models.CharField(max_length=300, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    sites = models.ManyToManyField(Site)
    

    def __str__(self):
        return self.title
    
    def get_thumb(self):
        im = get_thumbnail(self.photo, '200x200', crop='center', quality=99)
        return im.url # remember that sorl objects have url/width/height attributes
        
    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', [self.id])

    def sites_str(self):
        return ', '.join([s.name for s in self.sites.all()])
    sites_str.short_description = 'sites'
    
@python_2_unicode_compatible
class Vote(models.Model):
    """A Vote on a Product"""
    user = models.ForeignKey(User, related_name='votes')
    post = models.ForeignKey(Post)
    site = models.ForeignKey(Site)
    score = models.FloatField()

    def __str__(self):
        return "Vote"