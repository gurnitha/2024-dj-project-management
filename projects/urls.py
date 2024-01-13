from django.urls  import  path
from . import  views

urlpatterns  =  [
	path('home', views.home, name = 'home'),
	# path('projects', views.projects, name = 'projects'),
	path('projects', views.projectList, name = 'projects'),
	path('projects/<int:pk>', views.projectDetail, name ='project-detail'),
	path('tasks', views.taskList, name ='tasks'),
	# path('tasks', views.TaskListView.as_view(), name ='tasks'),
	path('create-task', views.taskCreate, name ='create-task'),
	path('tasks/<int:pk>', views.taskDetail, name ='task-detail'),

	# CRUD
	path('create-project', views.ProjectCreateView.as_view(), name ='create-project'),
]