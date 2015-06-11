from django.shortcuts import render


def post(request, postid):
    return render(request, 'post.html', {
        'PageTitle': "Post",
    })


def timeline_home(request):
    return render(request, 'timeline.html', {
        'PageTitle': "Myfilm - Timeline",
    })


def notifications(request):
    return render(request, 'notifications.html', {
        'PageTitle': "Notifications",
    })