from __future__ import unicode_literals

from django.db import models

# Create your models here.






class News(models.Model):
    """
    Description: News Description
    """
    time_stamp = models.CharField(max_length=128)
    website=models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    title = models.CharField(max_length=20)
    content = models.TextField()


