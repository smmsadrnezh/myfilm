from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^movie/$', 'myfilm.views.movie', name='salam'),

    url(r'^admin/', include(admin.site.urls)),
]
