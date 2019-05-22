from django.db import models
from django.utils import timezone
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name    

class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    category = models.ForeignKey(Category, default="general",on_delete=models.CASCADE,) # a foreignkey
    
    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title  




class Contact(models.Model):
 

  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name


     
