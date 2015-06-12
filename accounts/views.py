from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html', dict(c, **{'PageTitle': "Login"}))


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/timeline')
    else:
        return HttpResponseRedirect('/invalid')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/home')

def accounts_lists(request):
    return render(request, 'users.html', {
        'PageTitle': "Users",
    })


def register(request):
    return render(request, 'register.html', {
        'PageTitle': "Register",
    })


def profile(request, userid):
    return render(request, 'masoud.html', {
        'PageTitle': "Masoud - Profile",
    })


def forget_password(request):
    return render(request, 'forget.html', {
        'PageTitle': "Forget",
    })


def edit_profile(request, userid):
    return render(request, 'settings.html', {
        'PageTitle': "Settings",
    })


def change_password(request):
    return render(request, 'changepass.html', {
        'PageTitle': "Change Password",
    })


def lists(request):
    return render(request, 'lists.html', {
        'PageTitle': "List",
    })
