from django.contrib import admin
from .models import Movie, Artist, MovieArtist
from social.models import Post, Comment, Like, MovieRating
from chat.models import ChatMessage

admin.site.register(Movie)
admin.site.register(Artist)
admin.site.register(MovieArtist)
admin.site.register(ChatMessage)