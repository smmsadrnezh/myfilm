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