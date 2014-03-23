from django.shortcuts import render, HttpResponseRedirect
from sandbox.forms import SigninForm

def index(request):
    return render(request, "signin.html")

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/about/')
    else:
        form = SigninForm()
    return render(request, "signin.html", {'form' : form})

def signup(request):
    return render(request, "signup.html")


def forget_pass(request):
    return render(request, "forget_pass.html")

def about(request):
    return render(request, "about.html")
