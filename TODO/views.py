from django.shortcuts import render,redirect
import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from . models import Category
from . models import TodoList
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as messagess
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# @login_required(login_url="login/")
def index(request): 
    todos =TodoList.objects.filter(admin_id=request.user)
    categories= Category.objects.all()
    
    if request.method == "POST": 
        if "taskAdd" in request.POST: 
            title = request.POST["description"] 
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] 
            content = title + " -- " + date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category),admin=request.user)
            Todo.save() 
            return redirect("index") 
     
    return render(request, "TODO/index.html",{"todos":todos,"categories":categories})   

def deleteall(request):
    TodoList.objects.filter().delete()
    return redirect('index')  

def delete(request,id):
    if request.method=='POST':
        TodoList.objects.filter(id=id).delete()
        return redirect('index')


def register(request):
  if request.method=='POST':
   #Get form values
   first_name = request.POST['first_name']
  #  last_name = request.POST['last_name']
   username = request.POST['username']
   email = request.POST['email']
   password = request.POST['password']
   if password == password:
     # check username
        if User.objects.filter(username=username).exists():
            messages.error(request,'This username is already taken')
            return redirect('register')
        else:  
            if User.objects.filter(email=email).exists():
               messages.error(request,'This email is already taken')
               return redirect('register') 
            else:
              user = User.objects.create_user(username=username,password=password,email=email,
              first_name=first_name) 
              user.save()
              messages.success(request,'you are now registerd and login')
              return redirect('login')
   else:
    messages.error(request,'passwords do not match')
    return redirect('register')   
  else:      
    return render(request,'TODO/register.html')

def login(request):
  if request.method=='POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username,password=password)

    if user is not None:
          if user.is_active:
              auth.login(request,user)
              messages.success(request,'logged in')
              return redirect('index')

    else:
        messages.error(request,'Invalid Details') 
        return redirect('login')   

  else:      
    return render(request, 'TODO/login.html')
def logout(request):
    if request.method=='POST':
      auth.logout(request)
      messages.success(request,'you are logged out')
      return redirect('login')