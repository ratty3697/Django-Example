from __future__ import unicode_literals

from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=200)
    data = models.CharField(max_length = 5000)
    pub_date = models.DateTimeField('date published')
    user = models.CharField(max_length=30)
