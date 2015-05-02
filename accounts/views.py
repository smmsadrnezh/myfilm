from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def login(request):
    title = "Login"
    template = get_template('login.html')
    pageHtml = template.render()
    template = get_template('layout.html')
    html = template.render(Context({'pageBody': pageHtml , 'PageTitle': title}))
    return HttpResponse(html)


def users(request):
    title = "Users"
    template = get_template('users.html')
    pageHtml = template.render()
    template = get_template('tlayout.html')
    html = template.render(Context({'pageBody': pageHtml , 'PageTitle': title}))
    return HttpResponse(html)


def register(request):
   title = "Register"
   t = get_template('register.html')
   pageHtml = t.render()
   t = get_template('layout.html')
   html = t.render(Context({'pageBody': pageHtml , 'PageTitle': title}))
   return HttpResponse(html)


def masoud(request):
    title = "Masoud"
    t = get_template('masoud.html')
    pageHtml = t.render()
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml , 'PageTitle': title}))
    return HttpResponse(html)


def forget(request):
    title = "Forget"
    t = get_template('forget.html')
    pageHtml = t.render()
    t = get_template('layout.html')
    html = t.render(Context({'pageBody': pageHtml , 'PageTitle': title}))
    return HttpResponse(html)