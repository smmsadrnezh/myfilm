from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


def search(request):
    name = "search"
    template = get_template('search.html')
    pageHtml = template.render(Context({'mtitle': name}))
    template = get_template('layout.html')
    html = template.render(Context({'pageBody': pageHtml}))
    return HttpResponse(html)