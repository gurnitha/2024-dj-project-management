# 2024-dj-project-management
Build a project management using Django 5.x


## 1. SETUP

#### 1. Install django 5.0

        λ python -m venv venv3125x
        λ venv3125x\Scripts\activate.bat
        (venv3125x) λ pip install django

        modified:   README.md
        new file:   requirements.txt


## 2. DJANGO PROJECT AND APPS

#### 1. Create project

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

#### 2. Create app 'projects'

        modified:   README.md
        new file:   projects/__init__.py
        new file:   projects/admin.py
        new file:   projects/apps.py
        new file:   projects/migrations/__init__.py
        new file:   projects/models.py
        new file:   projects/tests.py
        new file:   projects/views.py

#### 3. Register projects to config/settings.py

        modified:   README.md
        modified:   config/settings.py


## 3. TEMPLATES

#### 1. Create projects page

        modified:   README.md
        modified:   config/urls.py
        new file:   projects/templates/projects/projects.html
        new file:   projects/urls.py
        modified:   projects/views.py

#### 2. Create home page

        modified:   README.md
        modified:   config/settings.py
        modified:   projects/urls.py
        modified:   projects/views.py
        new file:   templates/index.html

#### 3. Django template engine

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/views.py

#### 4. Loops and conditionals in templates

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/views.py

        Note: 

        1. Create dummy data array
        2. Fetch it to views and render in projects page

        :)

#### 5. Add and load static files

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   projects/static/css/bootstrap.min.css
        new file:   projects/static/css/main.css
        modified:   projects/templates/projects/projects.html
        new file:   templates/base.html
        modified:   templates/index.html
        new file:   templates/navbar.html


## 4. MODELS

#### 1. Create Project and Task models and superuser
        
        > (venv3125x) λ python manage.py makemigrations
        > (venv3125x) λ python manage.py migrate
        > (venv3125x) λ python manage.py createsuperuser

        Username (leave blank to use 'ing'): superadmin
        Email address: superadmin@mail.com
        Password:superadmin
        Password (again):superadmin

        modified:   README.md
        modified:   config/settings.py
        new file:   projects/migrations/0001_initial.py
        modified:   projects/models.py


## 5. ORM

#### 1. Create projects and tasks from python inteface

```
	python

	E:\_WORKSPACE\2024\django\2024-dj-project-management(main -> origin)

	# Use the interface

	(venv3125x) λ python manage.py shell
	Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	(InteractiveConsole)
	
	# import models
	>>> from projects.models import Project, Task

	# create project objects
	>>> project1 = Project.objects.create(name="IOS app development")
	
	# check the results
	>>> print(project1)
	>>> print(project1)
	IOS app development
	>>> print(project1.date_created)
	2024-01-13 00:47:46.867128+00:00
	>>> print(project1.description)
	None

	# create task objects
	>>> task1 = Task.objects.create(title='Create interfaces',project=project1, description='Create interfaces for the IOS app')
	
	# check the result
	>>> task1.status
	'TO DO'

	# update task
	>>> task1.status = 'COMPLETED'
	>>> task1.save()
	>>> task1.status
	'COMPLETED'
	
	# delete task
	>>> task1.delete()
	(1, {'projects.Task': 1})
	
	# Retrieving objects
	>>> Project.objects.all()
	<QuerySet [<Project: IOS app development>, <Project: IOS app development>]>
	>>> project1.title = 'Android app development'

	# save projects
	>>> project1.save()
	>>> Project.objects.all()
	<QuerySet [<Project: IOS app development>, <Project: IOS app development>]>
	>>> project1.name = 'Android app development'
	>>> project1.save()

	# Retrieving objects
	>>> Project.objects.all()
	<QuerySet [<Project: Android app development>, <Project: IOS app development>]>
	>>> project2 = Project.objects.create(name='Web development', description='Project description')
	>>> project2.save()
	>>> Project.objects.all()
	<QuerySet [<Project: Android app development>, <Project: IOS app development>, <Project: Web development>]>

	# count projects
	>>> Project.objects.all().count()
	3

```

        modified:   README.md
        new file:   projects/migrations/0002_alter_task_options.py
        modified:   projects/models.py


## 6. CRUD

#### 1. Display all projects

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/urls.py
        modified:   projects/views.py

        :)

#### 2. Display project details

        modified:   README.md
        new file:   projects/templates/projects/project-detail.html
        modified:   projects/templates/projects/projects.html
        modified:   projects/urls.py
        modified:   projects/views.py

#### 3. Display all tasks of the logged-in user

        modified:   README.md
        new file:   projects/templates/projects/tasks.html
        modified:   projects/urls.py
        modified:   projects/views.py

        Note: Only task(s) of the logged-in user are displayed.

        :)

#### 4. Display details task of the logged-in user

        modified:   README.md
        new file:   projects/templates/projects/task-detail.html
        modified:   projects/templates/projects/tasks.html
        modified:   projects/urls.py
        modified:   projects/views.py

        Note:

        1. In tasklist all tasks of logged-in user showed up in tasklist page.
        2. There are 2 unassigned tasks and they are showed in tasklist page.
        3. Both assigned tasks and unassigned tasks could be display its detail.
        :: So, tasklist, unassigned tasks, and task-detail worked.

        :)

#### 4.1 Save views.py file as part of the no. 4 above

        modified:   README.md
        modified:   projects/views.py

        Note: I forgot to save views.py file. No changed was made.

#### 5. ModelForm - Create TaskForm

        modified:   README.md
        modified:   config/settings.py
        new file:   projects/forms.py
        new file:   projects/templates/projects/task-create.html
        modified:   projects/urls.py
        modified:   projects/views.py

        Note:

        1. Can not create a new task from the form.
        2. To use Generic Views to perform CRUD operations

        (:

#### 6. Generic views: ProjectCreateView

        modified:   README.md
        new file:   projects/templates/projects/project_create_form.html
        modified:   projects/templates/projects/tasks.html
        new file:   projects/templates/projects/tasks.html_ori.html
        modified:   projects/urls.py
        modified:   projects/views.py

        Note:

        It worked :)