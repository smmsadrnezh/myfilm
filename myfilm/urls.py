from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^movie/$', 'movies.views.movie', name='salam'),
    url(r'^$', 'myfilm.views.home', name='salam'),
    url(r'^admin/', include(admin.site.urls)),
]
