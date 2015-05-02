from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def home(request):
    t = get_template('home.html')
    pageHtml = t.render()
    t = get_template('layout.html')
    html = t.render(Context({'pageBody': pageHtml}))
    return HttpResponse(html)

def timelinehome(request):
    t = get_template('home.html')
    pageHtml = t.render()
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml}))
    return HttpResponse(html)