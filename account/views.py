from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def register(request):
    name = "register"
    t = get_template('register.html')
    pageHtml = t.render(Context({'mtitle': name}))
    t = get_template('layout.html')
    html = t.render(Context({'pageBody' : pageHtml}))
    return HttpResponse(html)