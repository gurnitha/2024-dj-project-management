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
