from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from accounts.models import Follow
from django.template.loader import get_template
from django.contrib.auth.forms import UserCreationForm

def login(request):
    invalid_html = ""

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/timeline')
        else:
            invalid_html = get_template('invalid.html').render()

    c = {}
    c.update(csrf(request))
    return render(request,'login.html', dict(c, **{'PageTitle': "Login" , 'invalid_html' : invalid_html}))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def accounts_lists(request):
    return render(request, 'users.html', {
        'PageTitle': "Users",
    })


def register(request):
    # if request.method == 'POST':

    return render(request, 'register.html', {
        'PageTitle': "Register",
    })


def profile(request, userid):
    followers = Follow.objects.filter(following_id=request.user.id)
    following = Follow.objects.filter(follower_id=request.user.id)

    return render(request, 'profile.html', {
        'PageTitle': "Masoud - Profile",
        'current_user': request.user,
        'followers' : followers,
        'following' : following
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
