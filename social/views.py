from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
def post(request):
    title = "Post"
    t = get_template('../social/templates/post.html')
    pageHtml = t.render()
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)


def timeline_home(request):
    title = "Myfilm - Timeline"
    t = get_template('post.html')
    pageHtml = t.render()
    t = get_template('timeline.html')
    pageHtml = t.render(Context({'pageBody': pageHtml}))
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)


def notifications(request):
    title = "Notifications"
    t = get_template('notifications.html')
    pageHtml = t.render()
    t = get_template('tlayout.html')
    html = t.render(Context({'pageBody': pageHtml, 'PageTitle': title}))
    return HttpResponse(html)