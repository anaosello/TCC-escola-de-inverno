from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore

from .forms import CreateUserForm, LoginForm, CreateTaskForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from . models import Task

# Create your views here.

def home(request):
    return render(request, 'index.html')

#registering
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()
            
            return redirect ('my-login')
        
    context = {'form':form}
    return render(request, 'register.html', context=context)


#login a user
def my_login(request):
    form = LoginForm

    if request.method =='POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:

                auth.login(request,user)
                return redirect("dashboard")
    
    context = {'form':form}

    return render(request, 'my-login.html',context=context)


#dashboard page
@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'profile/dashboard.html')

#create a task
@login_required(login_url='my-login')
def createTask(request):

    form = CreateTaskForm()

    if request.method == 'POST':

        form = CreateTaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)

            task.user = request.user

            form.save()

            return redirect ('view-task')
    
    context = {'form':form}

    return render(request, "profile/create-task.html", context=context)


#view a task
@login_required(login_url='my-login')
def viewTask(request):

    current_user = request.user.id

    task = Task.objects.all().filter(user=current_user)

    context = {'task': task}

    return render(request, 'profile/view-task.html', context=context)
    
#delete a task
def deleteTask(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == 'POST':

        task.delete()

        return redirect('view-task')
    
    return render(request,'profile/delete-task.html')

#logout a user
def user_logout(request):
    auth.logout(request)
    return redirect("home")









