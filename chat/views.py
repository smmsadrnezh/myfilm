from django.shortcuts import render

# Create your views here.

def history(request):
    return render(request, 'login.html')


def messages(request):
    return render(request, 'login.html')