from django.shortcuts import render
from django.contrib.auth import login, logout as do_logout
# Create your views here.
def index (request):
    return render(request, 'index.html')

def login (request):
    return render(request, 'login.html')

def logout (request):
    do_logout(request)
    return redirect( 'login.html')
