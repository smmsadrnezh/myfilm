from django.shortcuts import render
from myfilm.models import Artist
from myfilm.models import Movie

def home(request):
    return render(request, 'home.html', {
        'PageTitle': "Myfilm - Home",
    })


def movie(request):
    return render(request, 'movie.html', {
        'PageTitle': "Leon the Professional",
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

