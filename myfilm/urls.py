from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^movie/$', 'movies.views.movie', name='salam'),
    url(r'^accounts/login/$', 'accounts.views.login', name='salam'),
    url(r'^accounts/users/$', 'accounts.views.users', name='salam'),
    url(r'^accounts/register$', 'accounts.views.register', name='salam'),
    url(r'^$', 'myfilm.views.home', name='salam'),
    url(r'^admin/', include(admin.site.urls)),
]
