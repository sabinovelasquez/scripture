from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Movie(models.Model):
  name = models.CharField( max_length = 200 )
  year = models.DateTimeField('released')
  pub_date = models.DateTimeField('published')
  director = models.CharField( max_length = 200 )
  writer = models.CharField( max_length = 200 )
  def __unicode__(self):
    return "%s" % (self.name)

class Script(models.Model):
  script = models.ForeignKey(Movie, on_delete=models.CASCADE)
  act = models.CharField( max_length = 2 )
  sequence = models.IntegerField(default=0)
  description = models.TextField( max_length = 140 )
  image = models.FileField(upload_to = 'img/')
  def __unicode__(self):
    return "%s (%s)" % (self.script, self.sequence)
