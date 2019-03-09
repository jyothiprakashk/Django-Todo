from django.shortcuts import render,redirect
from . models import TodoList,Category
import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponse



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
            return redirect("/") 
    
    
        if "taskDelete" in request.POST: 
             
               if request.method=='POST':
                    TodoList.objects.filter(id=id).delete()
                    return redirect('/')
                    

                   
    return render(request, "TODO/index.html", {"todos": todos, "categories":categories})   

def deleteall(request):
    TodoList.objects.filter().delete()
    return redirect('index')  

def delete(request,id):
    if request.method=='POST':
        TodoList.objects.filter(id=id).delete()
        return redirect('/')
