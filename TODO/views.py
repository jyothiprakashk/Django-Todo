from django.shortcuts import render,redirect
# from . models import TodoList,Category
import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from . models import Category
from . models import TodoList,Contact
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as messagess

@login_required(login_url="login/")
def index(request): 
    todos = TodoList.objects.all()
    categories = Category.objects.all() 
    if request.method == "POST": 
        if "taskAdd" in request.POST: 
            title = request.POST["description"] 
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] 
            content = title + " -- " + date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() 
            return redirect("index") 
    
    
        if "taskDelete" in request.POST: 
             
               if request.method=='POST':
                    TodoList.objects.filter(id=id).delete()
                    return redirect('index')
                    

                   
    return render(request, "TODO/index.html", {"todos": todos, "categories":categories})   

def deleteall(request):
    TodoList.objects.filter().delete()
    return redirect('index')  

def delete(request,id):
    if request.method=='POST':
        TodoList.objects.filter(id=id).delete()
        return redirect('index')
# @login_required(login_url="accounts/login/")
# def login(request):
#     return render(request,"accounts/register.html")




@login_required
def todos_for_user(request):
    todo = TodoList.objects.filter(user=request.user)
    return render(request, 'TODO/index.html', {'todos' : todo})

