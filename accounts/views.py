from django.shortcuts import render


def login(request):
    return render(request, 'login.html', {
    'PageTitle': "Login",
    })


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