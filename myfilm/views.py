import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from social.models import Post
import social.views
import accounts.views
from myfilm.models import MovieArtist
from social.models import MovieRating
from myfilm.models import Artist
from myfilm.models import Movie


def home(request):
    return render(request, 'home.html', {
        'PageTitle': "Myfilm",
    })


@login_required
def movie(request, movietitle):
    # process new post form (movie review)
    if request.method == 'POST':
        print()
        new_post = Post(body=request.POST.get('post_body', ''), title=request.POST.get('postTitle', ''),
                        created_time=datetime.datetime.now(), movie_id=Movie.objects.get(title=movietitle).id,
                        username_id=request.user.id)
        new_post.save()
        return HttpResponseRedirect('/posts/' + str(new_post.id))

    # calculating movie rate
    cur_movie = Movie.objects.get(title=movietitle)
    total_rate = calc_movie_rate(cur_movie.id)

    # fetch movie artists
    director = MovieArtist.objects.filter(movie_id=cur_movie.id, role='director')
    if len(director) > 0:
        director = director[0]
    writer = MovieArtist.objects.filter(movie_id=cur_movie.id, role='writer')
    if len(writer) > 0:
        writer = writer[0]
    stars = MovieArtist.objects.filter(movie_id=cur_movie.id, role='actor')

    return render(request, 'movie.html', {
        'PageTitle': " - " + cur_movie.title,
        'rate': total_rate,
        'movie': cur_movie,
        'director': director,
        'writer': writer,
        'stars': stars,
        'who_to_follows': social.views.who_to_follow(request),
        'recom_movies': social.views.movies_recommended(request),
        'popular_movies': social.views.popular_movies(request),
        'chat_users': accounts.views.followings(request.user),
        'notifications': social.views.notification_get(request.user.id)
    })


@login_required
def movies_list(request):
    movie_rate = {}
    for movie in Movie.objects.all().order_by('year'):
        movie_rate[movie] = calc_movie_rate(movie.id)

    return render(request, 'movies.html', {
        'PageTitle': " - All Movies",
        'movies': movie_rate,
        'who_to_follows': social.views.who_to_follow(request),
        'recom_movies': social.views.movies_recommended(request),
        'popular_movies': social.views.popular_movies(request),
        'chat_users': accounts.views.followings(request.user),
        'notifications': social.views.notification_get(request.user.id)
    })


@login_required
def artists_list(request):
    return render(request, 'artists.html', {
        'PageTitle': " - All Artists",
        'artists': Artist.objects.all().order_by('name'),
        'who_to_follows': social.views.who_to_follow(request),
        'recom_movies': social.views.movies_recommended(request),
        'popular_movies': social.views.popular_movies(request),
        'chat_users': accounts.views.followings(request.user),
        'notifications': social.views.notification_get(request.user.id)
    })


@login_required
def artist(request, artistname):
    return render(request, 'artist.html', {
        'PageTitle': " - " + artistname,
        'artist': Artist.objects.get(name=artistname),
        'who_to_follows': social.views.who_to_follow(request),
        'recom_movies': social.views.movies_recommended(request),
        'popular_movies': social.views.popular_movies(request),
        'chat_users': accounts.views.followings(request.user),
        'notifications': social.views.notification_get(request.user.id)
    })


def calc_movie_rate(movie_id):
    cur_movie_voters = MovieRating.objects.filter(movie_id=movie_id)
    total_rate = 0
    for voter in cur_movie_voters:
        total_rate += voter.rate
    if total_rate != 0:
        total_rate /= len(cur_movie_voters)
    return total_rate
