from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def post(request):
    title = "Post"
    t = get_template('post.html')
    pageHtml = t.render()
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)