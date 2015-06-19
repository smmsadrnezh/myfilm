from django.core.context_processors import csrf
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.template import Context
from django.shortcuts import render
from django.contrib import auth

from accounts.models import CustomUser
from .forms import CustomRegistration
from accounts.models import Follow
from myfilm.models import Movie
from social.models import Post
import social.views
import datetime


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
            'who_to_follows': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request),
            'chat_users': followings(request.user),
            'followers': followers(CustomUser.objects.filter(username=request.user.username)[0]),
            'following': followings(CustomUser.objects.filter(username=request.user.username)[0]),
            'follow_text': "Follow / Unfollow"
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
        profile_user = CustomUser.objects.filter(username=username)[0]
        if request.method == "POST":
            if request.POST.get('type', '') == "setting":
                # edit user setting
                CustomUser.objects.filter(id=request.user.id).update(
                    username=request.POST.get('username', ''),
                    first_name=request.POST.get('first_name', ''),
                    last_name=request.POST.get('last_name', ''),
                    email=request.POST.get('email', ''),
                    birth_date=request.POST.get('birth_date', '')
                )
                profile_user = CustomUser.objects.filter(username=request.POST.get('username', ''))[0]
            elif request.POST.get('type', '') == "change_password":
                # change user password
                if request.POST.get('password', '') == request.POST.get('conf_password', ''):
                    request.user.set_password(request.POST.get('password', ''))
                    request.user.save()
                else:
                    return HttpResponseRedirect('/chpass')
            else:
                # add or remove follower
                time = datetime.datetime.now()
                follower_id = request.user.id
                following_id = profile_user.id
                if is_following(request.user, profile_user):
                    Follow.objects.filter(follower_id=follower_id, following_id=following_id).delete()
                else:
                    Follow(time=time, follower_id=follower_id, following_id=following_id).save()

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
            'following': followings(profile_user),
            'following_count': len(followings(profile_user)),
            'followers_count': len(followers(profile_user)),
            'posts': all_posts,
            'who_to_follows': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request),
            'chat_users': followings(request.user),
            'follow_key': follow_key(request.user, profile_user, request)
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
            'who_to_follows': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request)
        })


def change_password(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'changepass.html', {
            'PageTitle': "Change Password",
            'who_to_follows': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request)
        })


def lists(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'lists.html', {
            'PageTitle': "List",
            'who_to_follows': social.views.who_to_follow(request),
            'recom_movies': social.views.movies_recommended(request),
            'popular_movies': social.views.popular_movies(request)
        })


def follow_key(user, profile_user, request):
    follow_html = ""
    button_text = "Follow"
    if user != profile_user:
        if is_following(user, profile_user):
            button_text = "Unfollow"
        c = {}
        c.update(csrf(request))
        follow_html = get_template('follow_key.html').render(Context(dict(c, **{'button_text': button_text})))
    return follow_html


def is_following(user, profile_user):
    for following in followings(user):
        if following == profile_user:
            return True
    return False