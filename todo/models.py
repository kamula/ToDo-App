from email.policy import default
import uuid
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    '''Create Category Form'''
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Todo(models.Model):
    '''Create Todo Class'''
    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ]
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    scheduled_time = models.DateTimeField()
    status = models.CharField(
        max_length=50, blank=True, null=True, choices=STATUS_CHOICES,default='pending')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
