from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# SignUp function
def signup(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # To get the clean data
            user = form.cleaned_data.get('username')
            # To throw a mesage to the template
            messages.success(request, "Account was created for " + user)
            return redirect('login')
            
    context = {
        'form':form
    }

    return render(request, 'HNC_app/signup.html', context)

# Login function
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}

    return render(request, 'HNC_app/login.html', context)

# Logout function
def logoutUser(request):

    logout(request)
    return redirect('login')
