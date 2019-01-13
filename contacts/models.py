from django.db import models
from datetime import datetime

class Contact(models.Model):
	listing = models.CharField(max_length=200)
	listing_id = models.IntegerField()
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=20)
	phone =  models.CharField(max_length=20)
	user_id = models.IntegerField(blank=True)
	message = models.TextField(blank=True)
	contact_date = models.DateTimeField(default=datetime.now,blank=True)

def __str__(self):
	return self.name
