from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def training(request):
    return render(request, 'training.html')

def job(request):
    return render(request, 'jobs.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact_us.html')

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
