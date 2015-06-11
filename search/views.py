from django.shortcuts import render
from .forms import SearchForm
from accounts.models import User
from myfilm.models import Movie

def search(request):
    if request.method=='Post':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
        movies = Movie.objects.filter(title=title)
        users = User.objects.filter(username = title)
        movies="fight club"
        return render(request, 'search.html', {
            'movie': movies, 'user' : users
        })
    return render(request, 'search.html', {

    })