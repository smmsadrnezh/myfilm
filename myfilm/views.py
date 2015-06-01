from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def home(request):
    title = "Myfilm - Home"
    t = get_template('home.html')
    pageHtml = t.render()
    t = get_template('layout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)


def timelinehome(request):
    title = "Myfilm - Timeline"
    t = get_template('post.html')
    pageHtml = t.render()
    t = get_template('timeline.html')
    pageHtml = t.render(Context({'pageBody': pageHtml}))
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)


def movie(request):
    title = "Leon the Professional"
    t = get_template('movie.html')
    pageHtml = t.render()
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)


def artists(request):
    title = "Artists"
    template = get_template('artists.html')
    pageHtml = template.render()
    template = get_template('tlayout.html')
    html = template.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)


def artist(request):
    title = "Tom Hanks"
    template = get_template('artist.html')
    pageHtml = template.render()
    template = get_template('tlayout.html')
    html = template.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)