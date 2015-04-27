from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def movie(request):
    name = "Movie Name"
    t = get_template('movie.html')
    pageHtml = t.render(Context({'mtitle': name}))
    t = get_template('layout.html')
    html = t.render(Context({'pageBody' : pageHtml}))
    return HttpResponse(html)