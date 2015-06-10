from django.shortcuts import render
from myfilm.models import Artist

def home(request):
    return render(request, 'home.html', {
        'PageTitle': "Myfilm - Home",
    })


def movie(request):
    return render(request, 'movie.html', {
        'PageTitle': "Leon the Professional",
    })


def movies_list(request):
    return render(request, 'movies.html')


def artists_list(request):
    artists = Artist.objects.all()
    return render(request, 'artists.html', {
        'artists':artists
    })


def artist(request, artistid):

    return render(request, 'artist.html', {
        'PageTitle': "Tom Hanks",
    })

