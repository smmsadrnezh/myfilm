from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def artists(request):
    name = "artist"
    template = get_template('artists.html')
    pageHtml = template.render(Context({'mtitle': name}))
    template = get_template('layout.html')
    html = template.render(Context({'pageBody': pageHtml}))
    return HttpResponse(html)

def tomhanks(request):
    name = "Tom Hanks"
    template = get_template('tomhanks.html')
    pageHtml = template.render(Context({'mtitle': name}))
    template = get_template('layout.html')
    html = template.render(Context({'pageBody': pageHtml}))
    return HttpResponse(html)