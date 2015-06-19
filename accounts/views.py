from django.core.context_processors import csrf
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.template import Context

import social.views
from accounts.models import CustomUser
from .forms import CustomRegistration
from accounts.models import Follow
from myfilm.models import Movie
from social.models import Post


def login(request):
    invalid_html = ""

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/timeline')
        else:
            invalid_html = get_template('invalid.html').render()

    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', dict(c, **{'PageTitle': "Login", 'invalid_html': invalid_html}))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def accounts_lists(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'users.html', {
            'PageTitle': "Users",
            'current_user': request.user,
            'following_users': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request),
            'chat_users': followings(request.user)
        })


def register(request):
    if request.method == 'POST':
        form = CustomRegistration(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    args = {}
    args.update(csrf(request))
    args['form'] = CustomRegistration()
    return render(request, 'register.html', dict(args, **{'PageTitle': "Login"}))


def followings(user):
    followings = []
    for following in Follow.objects.filter(follower_id=user.id):
        followings += CustomUser.objects.filter(id=following.following_id)
    return followings


def followers(user):
    followers = []
    for follower in Follow.objects.filter(following_id=user.id):
        followers += CustomUser.objects.filter(id=follower.follower_id)
    return followers


def profile(request, username):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:

        # finding profile user followers and followings
        profile_user = CustomUser.objects.filter(username=username)[0]
        posts = Post.objects.filter(username_id=profile_user.id).order_by('created_time')
        writer = CustomUser.objects.filter(id=profile_user.id)[0]

        all_posts = []
        for post in posts:
            movie = Movie.objects.filter(id=post.movie_id)[0]
            all_posts.append((post, movie, writer))

        return render(request, 'profile.html', {
            'PageTitle': "Myfilm - " + profile_user.first_name + " " + profile_user.last_name + " Profile",
            'profile_user': profile_user,
            'followers': followers(profile_user),
            'current_user': request.user,
            'following': followings(profile_user),
            'following_count': len(followings(profile_user)),
            'followers_count': len(followers(profile_user)),
            'posts': all_posts,
            'following_users': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request),
            'chat_users': followings(request.user),
            'follow_key': follow_key(request.user, profile_user)
        })


def forget_password(request):
    return render(request, 'forget.html', {
        'PageTitle': "Forget"
    })


def edit_profile(request, username):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'settings.html', {
            'PageTitle': "Settings",
            'current_user': request.user,
            'following_users': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request)
        })


def change_password(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'changepass.html', {
            'PageTitle': "Change Password",
            'current_user': request.user,
            'following_users': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request)
        })


def lists(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'lists.html', {
            'PageTitle': "List",
            'current_user': request.user,
            'following_users': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request)
        })


def follow_key(user, profile_user):
    follow_html = ""
    button_text = "Follow"
    if user != profile_user:
        for following in followings(user):
            if following == profile_user:
                button_text = "Unfollow"
        follow_html = get_template('follow_key.html').render(Context({'button_text': button_text}))
    return follow_html