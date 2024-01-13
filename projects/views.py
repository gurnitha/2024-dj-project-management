from django.shortcuts import render
from .models import Project 

# Create your views here.

def home(request):
	return render(request, 'index.html')

def projects(request):

	projects = [
		{
			'id':1,
			'title':'PROJECT A' 
		},
		{
			'id':2,
			'title':'PROJECT B' 
		}
	]

	context = {'projects': projects}
	return render(request, 'projects/projects.html', context)


def projectList(request):
	projects = Project.objects.all()
	context = {'projects':projects}
	return render(request, 'projects/projects.html',context)