from __future__ import unicode_literals

from django.db import models

# Create your models here.
class student_details(models.Model):
    Name= models.CharField(max_length=200)
    Mark= models.IntegerField('date published')


