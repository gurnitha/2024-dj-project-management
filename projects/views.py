from django.shortcuts import render
from django.shortcuts import get_object_or_404

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


def projectDetail(request,pk):
	project = get_object_or_404(Project, id=pk)
	project_tasks = project.task_set.all() # task_set.all() query, retrieves all the tasks related to a given project
	context = {'project':project,'project_tasks':project_tasks} 
	return render(request, 'projects/project-detail.html',context)