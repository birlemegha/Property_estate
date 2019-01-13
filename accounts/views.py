from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.


def register(request):
	if request.method == 'POST':
		
		#GET Form Inputs
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']

		#check password match
		if password == password2 :
			# check username already taken
			if User.objects.filter(username=username).exists():
				messages.error(request,'Username already taken')
				return redirect('register')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request,'Email already Have')
					return redirect('register')
				else:
					user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
					user.save()
					messages.success(request,'Successfully register')
					return redirect('login')


		else:
			messages.error(request, 'passwords not match')
			return redirect('register')

		
	else: 
		return render(request, 'accounts/register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			messages.success(request,'Successfully login')
			return redirect('dashboard')
		else:
			messages.error(request,'Invalid Credentials')
			return redirect('login')
	else: 
		return render(request, 'accounts/login.html')


def logout(request):
	if request.method == "POST":
		auth.logout(request)
		messages.success(request,'You are Logged Out')
		return redirect('index')



def dashboard(request):

	enquiry_listing = Contact.objects.all().filter(user_id=request.user.id)
	context = {
	'enquiry' : enquiry_listing
	}
	return render(request, 'accounts/dashboard.html',context)