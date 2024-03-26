from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def loginpage(request):
    return render(request,"accounts/loginpage.html")


def line_login_callback(request):
    return HttpResponse("You've successfully logged in with LINE!")

@login_required
def profile(request):
    user = request.user
    first_name = user.first_name
    last_name = user.last_name
    return render(request, 'accounts/profile.html', {'first_name': first_name, 'last_name': last_name})

def logout_view(request):
    logout(request)
    return redirect('/')