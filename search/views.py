from django.shortcuts import render

from .forms import SearchForm
from accounts.models import User
from myfilm.models import Movie
import social.views
import accounts.views
from django.http import HttpResponseRedirect


def search(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        form = SearchForm(request.POST)
        # if request.method == 'Post':
        if form.is_valid():
            title = form.cleaned_data['title']
        movies = Movie.objects.filter(title=title)
        users = User.objects.filter(username=title)
        return render(request, 'search.html', {
            'pageTitle': "Myfilm - Search",
            'movie': movies,
            'user': users,
            'current_user': request.user,
            'following_users': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request),
            'chat_users': accounts.views.followings(request.user)
        })
        form = SearchForm()
        return render(request, 'search.html', {'form': form, 'current_user': request.user
        })