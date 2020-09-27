from django.db import models
from django.contrib.auth.models import User
from datetime import date 

class Employee(models.Model):
	eid = models.IntegerField()
	ename = models.CharField(max_length=100)
	ejoin = models.CharField(max_length=100,null=True)
	econtact = models.IntegerField()
	eage = models.IntegerField()
	add = models.BooleanField(default=True)


	class Meta:
		ordering = ['-pk'] 

	def __str__(self):
		return f'{self.ename}'


class CompanyHead(models.Model):
	name = models.CharField(max_length=100,null=True)
	picture = models.ImageField(upload_to='images')
	position = models.CharField(max_length=100,null=True)
	joined_date = models.DateField(default=date.today)

	def __str__(self):
		return f'{self.name}'


class TopEmployee(models.Model):
	name = models.CharField(max_length=100,null=True)
	picture = models.ImageField(upload_to='images')
	position = models.CharField(max_length=100,null=True)
	joined_date = models.DateField(default=date.today)

	def __str__(self):
		return f'{self.name}'		
