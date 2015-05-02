from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def post(request):
    t = get_template('post.html')
    pageHtml = t.render()
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml}))
    return HttpResponse(html)