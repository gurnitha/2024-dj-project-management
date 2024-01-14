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

#### 6.1 (Re-save) Generic views: ProjectCreateView

        Note: I forgot to save views.py file. No changed was made.

#### 7. Generic views: ProjectUpdateView

        modified:   README.md
        modified:   projects/templates/projects/project-detail.html
        new file:   projects/templates/projects/project_update_form.html
        modified:   projects/urls.py
        modified:   projects/views.py

        :)

#### 8. Generic views: TasktUpdateView

        modified:   README.md
        new file:   projects/templates/projects/task_update_form.html
        modified:   projects/templates/projects/tasks.html
        modified:   projects/urls.py
        modified:   projects/views.py

        :)

#### 9. Add links to navbar: Projects, Tasks, Create Task, and Create Project

        modified:   README.md
        modified:   templates/navbar.html

        :)

#### 10. Generic views: ProjectDeleteView

        new file:   projects/templates/projects/project_confirm_delete.html
        modified:   projects/templates/projects/task-create.html
        modified:   projects/urls.py
        modified:   projects/views.py

        :)

#### 11. Generic views: TaskDeleteView

        modified:   README.md
        new file:   projects/templates/projects/task_confirm_delete.html
        modified:   projects/urls.py
        modified:   projects/views.py

        :)

#### 12. Join Task

        modified:   README.md
        modified:   projects/templates/projects/projects.html
        modified:   projects/templates/projects/task-detail.html
        modified:   projects/urls.py
        modified:   projects/views.py

        :)


## 7. USER AUTHENTICATION

#### 1. Create users app and register it to config/settings.py

        modified:   README.md
        modified:   config/settings.py
        new file:   users/__init__.py
        new file:   users/admin.py
        new file:   users/apps.py
        new file:   users/migrations/__init__.py
        new file:   users/models.py
        new file:   users/tests.py
        new file:   users/views.py

#### 2. User Registration

        modified:   config/urls.py
        new file:   users/templates/users/registration.html
        new file:   users/urls.py
        modified:   users/views.py

        Note: It has no logic yet to be able register a new user

#### 3. Add logic to User Registration

        modified:   README.md
        modified:   templates/navbar.html
        modified:   users/views.py

        Note:

        The signup form is now functional; we can sign up from our application. As you can see from the admin interface, the new user (test) does not have staff status and, therefore, cannot log in to the admin interface. We can also change the user permissions from the django admin interface.

#### 4. LoginView - To login the new user

        modified:   config/settings.py
        modified:   templates/navbar.html
        new file:   users/templates/users/login.html
        modified:   users/urls.py
        modified:   users/views.py

        Note:

        LoginView is a built-in class-based authentication view provided by django, which provides an easy way to log in to users in django. It handles all the login functionality in django by rendering the form, validating the data, and showing error messages if the user provides incorrect credentials when logging in.
        
        The LoginView uses the AuthenticationForm, a built-in form class from
        django.contrib.auth.forms. 

        The AuthenticationForm provides the built-in username and password fields. Open views.py and add the view for logging in users.

        As you can see above, the form will show the necessary error messages if the form is not valid. By default, the built in authentication system will redirect the user a profiles page

        To prevent seeing this error, we need to add a LOGIN_REDIRECT_URL in the settings .py file. Open the settings.py file and set the LOGIN_REDIRECT_URL to the tasks page.
        
        LOGIN_REDIRECT_URL ='tasks'

        # new user can login now :)

#### 5. Logout User - To logout the logged in user

        modified:   README.md
        modified:   templates/navbar.html
        modified:   users/urls.py
        modified:   users/views.py

        Note:

        Django also provides a built-in logout() function, which logouts the current user and clears the session data. 

        To log out a user, we call the logout function and pass the request object as shown in users/views.py: logout_user.

        # the logged in user is now can logout and redirect him to login page

        :)

#### 6. User Authorization

        modified:   README.md
        modified:   config/settings.py
        modified:   projects/views.py

        Note:

        User Authorization

        Authorization is the process of determining what an authenticated user can do. A superuser has all the permissions on the django system. 
        
        An unauthenticated user in django is called an anonymous user. 

        To restrict access to views to only authenticated users, Django uses the login_required decorator.

        1. Un-logged in user is now can not see projects or tasks
        2. To see projects or tasks, user must login first.
        3. If user want to see projects or tasks, but he has no account,
           then he has to signup first, and then login.

        :)

#### 7. Showing and hidding some menus to un-authenticated user

        modified:   README.md
        modified:   templates/navbar.html
        new file:   templates/navbar.html_old.html

        :)

#### 8. UserProfiles - Create Profile model

        modified:   README.md
        new file:   users/migrations/0001_initial.py
        modified:   users/models.py

#### 9. UserProfiles - Django signals

        modified:   users/admin.py
        modified:   users/models.py

        Django signals

        In simple terms, django signals work by notifying an application that an action has occurred elsewhere in the project. For example, we want a profile created every time a new user is created. To listen, receive and register a signal, django has a signal dispatcher that listens for signals throughout the application.
        
        A signal has a sender and a receiver. Let's define a signal receiver for creating a user profile. Open users/models.py and add the code below

        Note:

        1. Register Profile model to users/admin.py
        2. Create a new user
        3. New user was created and at the same time the profile also created

        :)

#### 10. UserProfiles - Profile update

        new file:   ing.jpeg
        new file:   users/forms.py
        modified:   users/models.py
        new file:   users/templates/users/profile-update-form.html
        modified:   users/urls.py
        modified:   users/views.py

        Note:

        1. Now we can update user profile 
           via http://127.0.0.1:8000/update-profile
           but could not upload photo.
        2. I modified the Profile model
           from : photo =models.ImageField()
           to 	: photo =models.ImageField(blank=True,null=True)
        3. Run migrations
        4. Fill in the Update profile form + update
        5. Photo still was not able to upload, but I kept it blank

        :)

#### 11. UserProfiles - Password reset
            
        modified:   users/templates/users/login.html
        new file:   users/templates/users/password-reset.html
        modified:   users/urls.py
        modified:   users/views.py

        Note:

        1. After clicking the Resset Password buttom, it shows like this:

        http://127.0.0.1:8000/reset_password
        Forbidden (403)
        CSRF verification failed. Request aborted.

        NEXT: Solving the problem by PasswordResetDoneView

        (:

#### 12. UserProfiles - PasswordResetDoneView

        modified:   README.md
        new file:   users/templates/users/password-reset-done.html
        modified:   users/urls.py

        Note:

        1. After clicking the Resset Password buttom, it shows like this:
           NoReverseMatch at /reset_password Reverse for 'password_reset_confirm' not found. 'password_reset_confirm' is not a valid view function or pattern name.

        2. But page look ok within this path: 
           http://127.0.0.1:8000/password_reset/done/

        (:











