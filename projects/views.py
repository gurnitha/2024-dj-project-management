from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'index.html')

def projects(request):
	context = {'project1': 'My first project'}
	return render(request, 'projects/projects.html', context)