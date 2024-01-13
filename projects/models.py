from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
	name = models.CharField(max_length=200,null=True,blank=True) 
	description = models.TextField(null=True,blank=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	date_updated = models.DateTimeField(auto_now=True,null=True,blank=True)

	def __str__(self):
		return self.title


class Task(models.Model):
	TODO="TO DO"
	COMPLETED='COMPLETED'
	INPROGRESS='IN-PROGRESS'

	STATUS_CHOICES = [
		(TODO, 'TO DO'),
		(COMPLETED, 'COMPLETED'),
		(INPROGRESS, 'IN-PROGRESS'),
	]

	title = models.CharField(max_length=150) 
	description = models.TextField(null=True,blank=True) 
	project = models.ForeignKey(Project,null=True,blank=True,on_delete=models.CASCADE)
	assignee = models.ForeignKey(User, null=True,blank=True, on_delete=models.SET_NULL)
	due_date = models.DateField(null=True,blank=True) 
	status = models.CharField(max_length=50,choices=STATUS_CHOICES,null=True,blank=True,default= TODO)
	date_created = models.DateTimeField(auto_now_add=True) 
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date_created']
