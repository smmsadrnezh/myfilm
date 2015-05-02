from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def artists(request):
    title = "Artists"
    template = get_template('artists.html')
    pageHtml = template.render()
    template = get_template('tlayout.html')
    html = template.render(Context({'pageBody': pageHtml , 'PageTitle': title}))
    return HttpResponse(html)


def tomhanks(request):
    title = "Tom Hanks"
    template = get_template('tomhanks.html')
    pageHtml = template.render()
    template = get_template('tlayout.html')
    html = template.render(Context({'pageBody': pageHtml , 'PageTitle': title}))
    return HttpResponse(html)