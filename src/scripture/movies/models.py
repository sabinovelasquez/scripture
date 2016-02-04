from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Movie(models.Model):
	name = models.Charfield( max_length = 200 )
	year = models.DateTimeField('release')
	pub_date = models.DateTimeField('published')
	# director = 