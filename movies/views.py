from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def movie(request):
    title = "Leon the Professional"
    t = get_template('movie.html')
    pageHtml = t.render()
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)