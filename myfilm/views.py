from django.shortcuts import render
from myfilm.models import Artist
from myfilm.models import Movie
from social.models import MovieRating

def home(request):
    return render(request, 'home.html', {
        'PageTitle': "Myfilm - Home",
    })


def movie(request,movietitle):
    cur_movie = Movie.objects.filter(title=movietitle)[0]
    cur_movie_voters = MovieRating.objects.filter(movie_id=cur_movie.id)
    total_rate = 0
    for voter in cur_movie_voters:
        total_rate += voter.rate
    if total_rate!=0:
        total_rate /= len(cur_movie_voters)
    return render(request, 'movie.html', {
        'rate':total_rate,'movie':cur_movie
    })


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html',{
        'movies': movies,
    })


def artists_list(request):
    artists = Artist.objects.all()
    return render(request, 'artists.html', {
        'artists':artists
    })


def artist(request,artistname):
    artist = Artist.objects.filter(name=artistname)[0]
    return render(request, 'artist.html', {
        'artist': artist,
    })

