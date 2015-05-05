from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^movies/1$', 'movies.views.movie', name='salam'),
    url(r'^search/$', 'search.views.search', name='salam'),
    url(r'^artists/$', 'artists.views.artists', name='salam'),
    url(r'^artists/tomhanks/$', 'artists.views.tomhanks', name='salam'),
    url(r'^accounts/login/$', 'accounts.views.login', name='salam'),
    url(r'^accounts/masoud/$', 'accounts.views.masoud', name='salam'),
    url(r'^accounts/masoud/settings$', 'accounts.views.settings', name='salam'),
    url(r'^accounts/lists$', 'accounts.views.lists', name='salam'),
    url(r'^accounts/masoud/settings/changepassword$', 'accounts.views.changepass', name='salam'),
    url(r'^accounts/masoud/notifications$', 'accounts.views.notifs', name='salam'),
    url(r'^accounts/users/$', 'accounts.views.users', name='salam'),
    url(r'^accounts/register/$', 'accounts.views.register', name='salam'),
    url(r'^accounts/forget/$', 'accounts.views.forget', name='salam'),
    url(r'^$', 'myfilm.views.home', name='salam'),
    url(r'^timeline/$', 'myfilm.views.timelinehome', name='salam'),
    url(r'^posts/$', 'posts.views.post', name='salam'),
    url(r'^admin/', include(admin.site.urls)),

]
