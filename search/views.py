from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template


def search(request):
    title = "Search"
    template = get_template('search.html')
    pageHtml = template.render()
    template = get_template('tlayout.html')
    html = template.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)