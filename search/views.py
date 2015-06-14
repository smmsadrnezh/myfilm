from django.shortcuts import render

from .forms import SearchForm
from accounts.models import User
from myfilm.models import Movie
from social.views import who_to_follw, movies_recommended, popular_movies


def search(request):
    if request.method == 'Post':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
        movies = Movie.objects.filter(title=title)
        users = User.objects.filter(username=title)
        return render(request, 'search.html', {
            'movie': movies,
            'user': users,
            'current_user': request.user,
            'following_users': who_to_follw(request),
            'recom_movies': movies_recommended(request),
            'popular_movies': popular_movies(request)
        })
    form = SearchForm()
    return render(request, 'search.html', {'form': form, 'current_user': request.user
    })