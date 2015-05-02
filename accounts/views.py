from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def login(request):
    name = "login"
    template = get_template('login.html')
    pageHtml = template.render(Context({'mtitle': name}))
    template = get_template('layout.html')
    html = template.render(Context({'pageBody': pageHtml}))
    return HttpResponse(html)


def users(request):
    name = "Arman"
    template = get_template('users.html')
    pageHtml = template.render(Context({'name': name}))
    template = get_template('tlayout.html')
    html = template.render(Context({'pageBody': pageHtml}))
    return HttpResponse(html)


def register(request):
    name = "register"
    t = get_template('register.html')
    pageHtml = t.render(Context({'mtitle': name}))
    t = get_template('layout.html')
    html = t.render(Context({'pageBody': pageHtml}))
    return HttpResponse(html)


def masoud(request):
    name = "Masoud"
    t = get_template('masoud.html')
    pageHtml = t.render(Context({'mtitle': name}))
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml}))
    return HttpResponse(html)


def forget(request):
    name = "forget"
    t = get_template('forget.html')
    pageHtml = t.render(Context({'mtitle': name}))
    t = get_template('layout.html')
    html = t.render(Context({'pageBody': pageHtml}))
    return HttpResponse(html)