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
  cover = models.FileField(upload_to='covers/')
  genre = models.CharField( max_length = 200 )
  def __unicode__(self):
    return "%s" % (self.name)

class Script(models.Model):
  ACT_I = 'I'
  ACT_II = 'II'
  ACT_III = 'III'
  ACT_CHOICES = (
    (ACT_I, 'ACT I'), (ACT_II, 'ACT II'), (ACT_III, 'ACT III'),
  )
  SEQ = [(i,i) for i in range(1,9)]

  script = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sequences')
  act = models.CharField( max_length = 2, choices=ACT_CHOICES, default= ACT_I )
  sequence = models.IntegerField( choices=SEQ, default= 1 )
  begin = models.CharField( max_length = 20 )
  end = models.CharField( max_length = 20 )
  description = models.TextField( max_length = 140 )
  image = models.FileField(upload_to = 'sequences/')
  def __unicode__(self):
    return "%s (%s)" % (self.script, self.sequence)
