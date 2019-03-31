from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse





class contact(models.Model):
	Email_id = models.CharField(max_length=20,unique=True)
	First_name= models.CharField(max_length=10)
	Last_name= models.CharField(max_length=10)
	phone_number = models.CharField(max_length=10)
	

	def __str__(self):
		return self.Email_id

	def get_absolute_url (self):
		return reverse('contact-detail' , kwargs={'pk':self.pk})
