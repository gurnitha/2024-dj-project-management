from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Project, Task 
from .forms import TaskForm

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


'''
	=============CRUD: Generic Views==================
'''

def taskCreate(request):

	'''
	In the code above, we first import the TaskForm at the top. Then we define a taskCreate
	function which takes a request object as a parameter. Inside the function, we instantiate the
	TaskForm and pass it to the template content if the request.method is GET.

	In the POST method, we check if the form is valid by calling form.is_valid() , and if the form
	is valid, we save the form data and create a new Task instance.
	'''
	form = TaskForm
	if request.method == "POST":
		form =TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('tasks')
	context = {'form':form}
	return render(request, 'projects/task-create.html',context)


# # Generic views: TaskListView
# from django.views.generic import ListView
# class TaskListView(ListView):
# 	model = Task
# 	template_name = 'projects/tasks.html'


# Generic views: ProjectCreateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Project
class ProjectCreateView(CreateView):
	model = Project
	fields = ["name","description"]
	template_name = 'projects/project_create_form.html'
	success_url = reverse_lazy('projects')


# Generic views: ProjectUpdateView
from django.views.generic.edit import CreateView, UpdateView
class ProjectUpdateView(UpdateView):
	model = Project
	template_name = 'projects/project_update_form.html'
	fields = ["name","description"]
	success_url = reverse_lazy('projects')


# Generic views: TaskUpdateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
class TaskUpdateView(UpdateView):
	model = Task
	template_name = 'projects/task_update_form.html'
	fields = ["title","description","project","assignee","due_date","status"]
	success_url = reverse_lazy('tasks')


# Generic views: ProjectDeleteView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
class ProjectDeleteView(DeleteView):
	model = Project
	template_name = 'projects/project_confirm_delete.html'
	success_url = reverse_lazy('projects')


# Generic views: TaskDeleteView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
class TaskDeleteView(DeleteView):
	model = Task
	template_name = 'projects/task_confirm_delete.html'
	success_url = reverse_lazy('tasks')


def joinTask(request,pk):
	task =Task.objects.get(id=pk)
	task.assignee=request.user
	task.save()
	return redirect('tasks')
