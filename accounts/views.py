from django.core.context_processors import csrf
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth

from .forms import CustomRegistration
from accounts.models import Follow
from accounts.models import CustomUser


def login(request):
    invalid_html = ""

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/timeline')
        else:
            invalid_html = get_template('invalid.html').render()

    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', dict(c, **{'PageTitle': "Login", 'invalid_html': invalid_html}))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def accounts_lists(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'users.html', {
            'PageTitle': "Users",
            'current_user': request.user,
        })


def register(request):
    if request.method == 'POST':
        form = CustomRegistration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    args = {}
    args.update(csrf(request))
    args['form'] = CustomRegistration()
    return render(request, 'register.html', dict(args, **{'PageTitle': "Login"}))


def profile(request, username):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        followings = []
        followers = []
        profile_user = CustomUser.objects.filter(username=username)[0]
        for follower in Follow.objects.filter(following_id=profile_user.id):
            followers += CustomUser.objects.filter(id=follower.follower_id)
        for following in Follow.objects.filter(follower_id=profile_user.id):
            followings += CustomUser.objects.filter(id=following.following_id)
        return render(request, 'profile.html', {
            'PageTitle': "Myfilm - " + profile_user.first_name + " " + profile_user.last_name + " Profile",
            'profile_user': profile_user,
            'followers': followers,
            'current_user': request.user,
            'following': followings,
            'following_count': len(followings),
            'followers_count': len(followers)
        })


def forget_password(request):
    return render(request, 'forget.html', {
        'PageTitle': "Forget",
    })


def edit_profile(request, username):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'settings.html', {
            'PageTitle': "Settings",
            'current_user': request.user,
        })


def change_password(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'changepass.html', {
            'PageTitle': "Change Password",
            'current_user': request.user,
        })


def lists(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'lists.html', {
            'PageTitle': "List",
            'current_user': request.user,
        })
