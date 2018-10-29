from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render 

def login_redirect(requests):
	return redirect('/accounts/login/')

def land(request):
	return render(request, 'accounts/land.html')
