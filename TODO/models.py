from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

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
    admin=models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title  






     
