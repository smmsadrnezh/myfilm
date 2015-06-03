from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template
# Create your views here.

def home(request):
    title = "Myfilm - Home"
    t = get_template('home.html')
    pageHtml = t.render()
    t = get_template('layout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)


def movie(request):
    title = "Leon the Professional"
    t = get_template('movie.html')
    pageHtml = t.render()
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)


def movies_list(request):
    return HttpResponse()


def artists_list(request):
    title = "Artists"
    template = get_template('artists.html')
    pageHtml = template.render()
    template = get_template('tlayout.html')
    html = template.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)


def artist(request, artistid):
    title = "Tom Hanks"
    template = get_template('artist.html')
    pageHtml = template.render()
    template = get_template('tlayout.html')
    html = template.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)