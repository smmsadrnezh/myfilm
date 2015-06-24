from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import SearchForm
from accounts.models import User
from myfilm.models import Movie
import social.views
import accounts.views


@login_required
def search(request):
    form = SearchForm(request.POST)
    # if request.met hod == 'Post':
    if form.is_valid():
        title = form.cleaned_data['title']
    return render(request, 'search.html', {
        'pageTitle': " - Search",
        'movie': Movie.objects.filter(title=title),
        'user': User.objects.filter(username=title),
        'who_to_follows': social.views.who_to_follow(request),
        'recom_movies': social.views.movies_recommended(request),
        'popular_movies': social.views.popular_movies(request),
        'chat_users': accounts.views.followings(request.user),
        'notifications': social.views.notification_get(request.user.id)
    })
    form = SearchForm()
    return render(request, 'search.html', {'form': form,
    })