#not sure if this file will be needed

'''
from django.db import models
import backend.functions as functions
from functions.register import register
from functions.login import login

class Register(models.model):
    username = models.CharField(max_length=63)
    password = models.CharField(max_length=63)
    result = register(username, password)

class Login(models.model):
    username = models.CharField()
    password = models.CharField()
    result = login(username, password)
'''