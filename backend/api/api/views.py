from django.http import HttpResponse

#importing functions from folder
import backend.functions as functions
from functions.register import register
from functions.login import login

current_user = ''

def register_user(request):
    result = 1
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        result = register(username, password)
    if result == 0:
        pass #should redirect to new page
    elif result == 2:
        pass #create message that username already exists
    else:
        pass #username and password too short or long

def login_user(request):
    result = 1
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        result = login(username, password)
    if result == 0:
        global current_user
        current_user = username
        pass #should redirect to new page
    elif result == 2:
        pass #create message invalid password for username
    else:
        pass #username doesn't exist
