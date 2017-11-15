from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm, UserForm
from basic_app.models import UserProfileInfo

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):

	context_dict = {}

	return render(request, 'basic_app/index.html', context=context_dict)

@login_required
def special(request):
	return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('basic_app:index'))

# Register View
def register(request):

	# Instantiate registered variable
	registered = False

	if request.method == 'POST':

		user_form = UserForm(data=request.POST)
		userprofile_form = UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and userprofile_form.is_valid():

			# user save
			user = user_form.save()

			# store password as hashed password
			user.set_password(user.password)
			user.save()

			## Update user_profile var with other details
			user_profile = userprofile_form.save(commit=False)
			user_profile.user = user

			if 'profile_pic' in request.FILES:
				user_profile.profile_pic = request.FILES['profile_pic']

			user_profile.save()

			registered = True
		else:

			print(user_form.errors, userprofile_form.errors)


	else:
		user_form = UserForm()
		userprofile_form = UserProfileInfoForm()

	# Create a context_dict
	context_dict = {
		'user_form':user_form,
		'userprofile_form':userprofile_form,
		'registered':registered,
	}

	return render(request, 'basic_app/registration.html', context=context_dict)

def user_login(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('basic_app:index'))

			else:
				return HttpResponse("ACCOUNT NOT ACTIVE")
		else:
			print("Someone tried to login and failed!")
			print("Username: {} and Password: {}".format(username, password))

			return HttpResponse("Invalid login details supplied.")

	else:

		return render(request, 'basic_app/login.html', {})
