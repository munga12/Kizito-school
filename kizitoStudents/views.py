from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'auth/login.html')
def signup(request):
    return render(request, 'auth/signup.html')