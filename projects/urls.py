from django.urls  import  path
from . import  views

urlpatterns  =  [
	path('home', views.home, name = 'home'),
	# path('projects', views.projects, name = 'projects'),
	path('projects', views.projectList, name = 'projects'),
	path('projects/<int:pk>', views.projectDetail, name ='project-detail'),
]