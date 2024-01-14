from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

'''
If the request is POST, we create an instance of the UserCreationForm using the
request.POST data. If the form is valid, we save the new user.

We then call the login() function to log in the user. Logging in the user after the registration
process allows us to give the user immediate access to the application's features.

The login() function creates a user session and allows the user to access authenticated user
features.
'''

# def registration(request):
# 	form = UserCreationForm
# 	context = {'form':form}
# 	return render(request, 'users/registration.html', context)


# REGISTER a new user
def registration(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			# return redirect('home')

	form = UserCreationForm
	context = {'form':form}
	return render(request, 'users/registration.html', context)


# LOGIN the registered user
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView
class UserLoginView(LoginView):
	template_name = 'users/login.html'
	form = AuthenticationForm


# LOGOUT the logged in user
from django.contrib.auth import login,logout
from django.shortcuts import render,redirect
def logout_user(request):
	logout(request)
	return redirect("login")