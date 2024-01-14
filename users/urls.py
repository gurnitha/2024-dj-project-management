from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	path('register', views.registration, name = 'register'),
	path('login', views.UserLoginView.as_view(), name = 'login'),
	path('logout', views.logout_user, name = 'logout'),
	path('update-profile', views.update_profile, name ='update-profile'),

	# Password reset
	path('reset_password', auth_views.PasswordResetView.as_view(
		template_name = 'users/password-reset.html'), name='password-reset'),
]