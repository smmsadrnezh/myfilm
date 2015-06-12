from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  # myfilm app urls
                  url(r'^$', 'myfilm.views.home'),
                  url(r'^movies$', 'myfilm.views.movies_list'),
                  url(r'^movies/(?P<movietitle>[1-9 a-z A-Z %\':.]+)$', 'myfilm.views.movie'),
                  url(r'^artists/$', 'myfilm.views.artists_list'),
                  url(r'^artists/(?P<artistname>[1-9 a-z A-Z %\':.]+)$', 'myfilm.views.artist'),

                  # search app urls
                  url(r'^search/$', 'search.views.search'),

                  # accounts app urls
                  url(r'^chpass$', 'accounts.views.change_password'),
                  url(r'^login/$', 'accounts.views.login'),
                  url(r'^logout/$', 'accounts.views.logout'),
                  url(r'^profile/(?P<username>[1-9 a-z A-Z %\':.]+)/$', 'accounts.views.profile'),
                  url(r'^profile/(?P<username>[1-9 a-z A-Z %\':.]+)/edit$', 'accounts.views.edit_profile'),
                  url(r'^register/$', 'accounts.views.register'),
                  url(r'^forget/$', 'accounts.views.forget_password'),
                  url(r'^accounts/$', 'accounts.views.accounts_lists'),


                  # chat app urls
                  url(r'^messages/$', 'chat.views.history'),
                  url(r'^messages/(?P<username>[1-9 a-z A-Z %\':.]+)/$', 'chat.views.messages'),

                  # social app urls
                  url(r'^timeline/$', 'social.views.timeline_home'),
                  url(r'^posts/(?P<postid>\d+)/$', 'social.views.post'),
                  url(r'^notifications$', 'social.views.notifications'),
                  url(r'^admin/', include(admin.site.urls)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)