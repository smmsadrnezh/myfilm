from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from accounts.models import CustomUser
from myfilm.models import Movie
import social.views
import accounts.views


@login_required
def search(request):
    if request.method == 'POST':
        return render(request, 'result_page.html', {
            'pageTitle': " - Search",
            'search_string': request.POST.get('search_string'),
            'movies_result': Movie.objects.filter(title__contains=request.POST.get('search_string')),
            'users_result': CustomUser.objects.filter(username__contains=request.POST.get('search_string')),
            'who_to_follows': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request),
            'chat_users': accounts.views.followings(request.user),
            'notifications': social.views.notification_get(request.user.id)
        })
    else:
        return HttpResponseRedirect('/timeline')


def ajax_search(request, search_string):
    return HttpResponse(render(request, 'result_ajax.html', {
        'search_string': search_string,
        'movies_search_results': CustomUser.objects.filter(username__contains=request.POST.get('search_string')),
        'users_search_results': CustomUser.objects.filter(username__contains=request.POST.get('search_string')),
    }))