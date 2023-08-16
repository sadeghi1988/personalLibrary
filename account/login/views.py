from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from . import models

@login_required
def home(request):
    print(request)
    return render(request, 'home.html')

def create_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']

        if models.CustomUser.objects.filter(username=username).exists():
            return HttpResponse("Username already exists. Please choose a different username.")

        new_user = models.CustomUser.objects.create_user(username=username, password=password)
        new_user.user_type = user_type
        new_user.save()
        # return HttpResponse("user created")  # Show an error message
        return redirect('/login/home') 


    elif request.method == 'GET':
        return render(request, 'create.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(request)
        user = authenticate(request, username=username, password=password)
        print(request.user)
        if user is not None:
            login(request, user)
            user_type = request.user.user_type
            # welcome_message = f"Welcome {request.user} , {user_type.capitalize()}!"
            # return redirect('/')  # Change 'profile' to the appropriate URL name
            # return HttpResponse(welcome_message, content_type="text/plain")
            return render(request, '/home')
        else:
            return HttpResponse("Invalid login credentials")  # Show an error message

    elif request.method == 'GET':
        return render(request, 'login.html')
