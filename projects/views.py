from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Project, Task 

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
	'''
	task_set.all() query, retrieves all the tasks 
	related to a given project
	'''
	project_tasks = project.task_set.all()
	context = {'project':project,'project_tasks':project_tasks} 
	return render(request, 'projects/project-detail.html',context)


def taskList(request):
	''' 
	fetches all the tasks assigned to the currently 
	logged-in user and other unassigned tasks.
	'''
	user_tasks =Task.objects.filter(assignee=request.user) 
	tasks = Task.objects.all().filter(assignee=None) # fetches  all  unassigned  tasks.
	# print(tasks)
	context = {'tasks':tasks,'user_tasks':user_tasks} 
	return render(request, 'projects/tasks.html',context)


def taskDetail(request,pk):
	task = get_object_or_404(Task, id=pk)
	context = {'task':task}
	return render(request, 'projects/task-detail.html',context)