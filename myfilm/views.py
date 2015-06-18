import social.views
from django.http import HttpResponseRedirect
import accounts.views
from myfilm.models import MovieArtist
from social.models import MovieRating
from django.shortcuts import render
from myfilm.models import Artist
from myfilm.models import Movie


def home(request):
    return render(request, 'home.html', {
        'PageTitle': "Myfilm - Home",
    })


def movie(request, movietitle):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        ###calculating movie rate

        cur_movie = Movie.objects.filter(title=movietitle)[0]
        total_rate = calc_movie_rate(cur_movie.id)
        ### end of calculating movie rate

        ### fetch movie artists

        director = MovieArtist.objects.filter(movie_id=cur_movie.id, role='director')
        if len(director) > 0:
            director = director[0]
        writer = MovieArtist.objects.filter(movie_id=cur_movie.id, role='writer')
        if len(writer) > 0:
            writer = writer[0]
        stars = MovieArtist.objects.filter(movie_id=cur_movie.id, role='actor')
        ### end fetching artists

        return render(request, 'movie.html', {
            'PageTitle': "Myfilm - " + cur_movie.title,
            'rate': total_rate,
            'movie': cur_movie,
            'director': director,
            'writer': writer,
            'stars': stars,
            'current_user': request.user,
            'following_users': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request),
            'chat_users': accounts.views.followings(request.user)
        })


def movies_list(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        movie_rate = {}
        for movie in Movie.objects.all().order_by('year'):
            movie_rate[movie] = calc_movie_rate(movie.id)

        return render(request, 'movies.html', {
            'PageTitle': "Myfilm - All Movies",
            'movies': movie_rate,
            'current_user': request.user,
            'following_users': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request),
            'chat_users': accounts.views.followings(request.user)
        })


def artists_list(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'artists.html', {
            'PageTitle': "Myfilm - All Artists",
            'artists': Artist.objects.all().order_by('name'),
            'current_user': request.user,
            'following_users': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request),
            'chat_users': accounts.views.followings(request.user)
        })


def artist(request, artistname):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'artist.html', {
            'PageTitle': "Myfilm - " + artistname,
            'artist': Artist.objects.filter(name=artistname)[0],
            'current_user': request.user,
            'following_users': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request),
            'chat_users': accounts.views.followings(request.user)
        })


def calc_movie_rate(movie_id):
    cur_movie_voters = MovieRating.objects.filter(movie_id=movie_id)
    total_rate = 0
    for voter in cur_movie_voters:
        total_rate += voter.rate
    if total_rate != 0:
        total_rate /= len(cur_movie_voters)
    return total_rate
