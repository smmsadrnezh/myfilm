from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {
        'PageTitle': "Myfilm - Home",
    })


def movie(request):
    return render(request, 'movie.html', {
        'PageTitle': "Leon the Professional",
    })


def movies_list(request):
    return render(request, 'movie.html')


def artists_list(request):
    return render(request, 'artists.html', {
        'PageTitle': "Artists",
    })


def artist(request, artistid):
    return render(request, 'artist.html', {
        'PageTitle': "Tom Hanks",
    })