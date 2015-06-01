from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^$', 'myfilm.views.home', name='salam'),
    url(r'^movies$', 'myfilm.views.movies_list', name='salam'),
    url(r'^movies/(?P<movieid>\d+)/$', 'myfilm.views.movie', name='salam'),
    url(r'^artists/$', 'myfilm.views.artists', name='salam'),
    url(r'^artists/(?P<artistid>\d+)/$', 'myfilm.views.artist', name='salam'),

    url(r'^search/$', 'search.views.search', name='salam'),

    url(r'^changepassword$', 'accounts.views.change_password', name='salam'),
    url(r'^accounts/login/$', 'accounts.views.login', name='salam'),
    url(r'^profile/(?P<userid>\d+)/$', 'accounts.views.profile', name='salam'),
    url(r'^profile/(?P<userid>\d+)/edit$', 'accounts.views.edit_profile', name='salam'),
    url(r'^register/$', 'accounts.views.register', name='salam'),
    url(r'^forget/$', 'accounts.views.forget_password', name='salam'),
    url(r'^accounts/lists$', 'accounts.views.lists', name='salam'),

    url(r'^messages/$', 'chat.views.history', name='salam'),
    url(r'^messages/(?P<userid>\d+)/$', 'chat.views.messages', name='salam'),

    url(r'^timeline/$', 'social.views.timeline_home', name='salam'),
    url(r'^posts/(?P<postid>\d+)/$', 'social.views.post', name='salam'),
    url(r'^notifications$', 'social.views.notifications', name='salam'),
    url(r'^admin/', include(admin.site.urls)),

]
