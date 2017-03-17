from __future__ import unicode_literals

from django.db import models
from django.db.models import Count


# Create your models here.
class student(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, null=False, error_messages = {'required' : "Please enter an name.",})
	address = models.CharField(max_length=30, null=False, error_messages = {'required' : "Please enter an  address."})
     