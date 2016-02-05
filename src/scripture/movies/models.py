from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import datetime




class Movie(models.Model):
  name = models.CharField( max_length = 200 )
  year = models.IntegerField(default = datetime.now().year )
  pub_date = models.DateTimeField('published')
  director = models.CharField( max_length = 200 )
  writer = models.CharField( max_length = 200 )
  cover = models.FileField(upload_to = 'img/')
  def __unicode__(self):
    return "%s" % (self.name)

class Script(models.Model):
  ACT_I = 'I'
  ACT_II = 'II'
  ACT_III = 'III'
  ACT_CHOICES = (
    (ACT_I, 'ACT I'), (ACT_II, 'ACT II'), (ACT_III, 'ACT III'),
  )
  script = models.ForeignKey(Movie, on_delete=models.CASCADE)
  act = models.CharField( max_length = 2, choices=ACT_CHOICES, default= ACT_I )
  sequence = models.IntegerField(default=0)
  description = models.TextField( max_length = 140 )
  image = models.FileField(upload_to = 'img/')
  def __unicode__(self):
    return "%s (%s)" % (self.script, self.sequence)
