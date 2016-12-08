from django.db import models
from django.utils import timezone

class Part(models.Model):
    name = models.CharField(max_length=200)
    type_parts = models.ForeignKey('Type_of_part')

class Request(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey('Client')
    problem = models.TextField;

class Client(models.Model):
    surname = models.CharField(max_length=30);
    name = models.CharField(max_length=30);
    tel = models.CharField(max_length=11);
    model = models.ForeignKey('Apple_model');

class Apple_model(models.Model):
    name = models.CharField(max_length=50);

class Type_of_part(models.Model):
    name = models.CharField(max_length=50);