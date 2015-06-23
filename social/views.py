import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from accounts.models import CustomUser
from accounts.models import Follow
from social.models import Comment
from accounts.models import User
from myfilm.models import Movie
from social.models import Post
from social.models import Like
import accounts.views


@login_required
def post(request, postid):
    if request.method == 'POST':
        # add new comment
        Comment(body=request.POST['body'], post_id=postid, username_id=request.user.id, time=datetime.datetime.now(),
                title=request.POST['title']).save()
        return HttpResponseRedirect('/posts/' + postid)

    likers = []
    for like in Like.objects.filter(post_id=postid):
        likers.append(User.objects.get(id=like.username_id))

    comments_dic = {}
    for comment in Comment.objects.filter(post_id=postid):
        writer = User.objects.get(id=comment.username_id)
        comments_dic[comment] = writer

    return render(request, 'post.html', {
        'PageTitle': " - Post",
        'writer': CustomUser.objects.get(id=post.username_id),
        'post': post,
        'movie': Movie.objects.get(id=post.movie_id),
        'likers': likers,
        'comments': comments_dic,
        'who_to_follows': who_to_follow(request),
        'recom_movies': movies_recommended(request),
        'popular_movies': popular_movies(request),
        'chat_users': accounts.views.followings(request.user)
    })


@login_required
def timeline_home(request):
    followings = Follow.objects.filter(follower_id=request.user.id)
    all_posts = []
    for following in followings:
        for post in Post.objects.filter(username_id=following.following_id).order_by('created_time'):
            movie = Movie.objects.get(id=post.movie_id)
            all_posts.append((post, movie, CustomUser.objects.get(id=following.following_id)))

    return render(request, 'timeline.html', {
        'PageTitle': " - Timeline",
        'posts': all_posts,
        'current_user': request.user,
        'who_to_follows': who_to_follow(request),
        'recom_movies': movies_recommended(request),
        'popular_movies': popular_movies(request),
        'chat_users': accounts.views.followings(request.user)
    })


@login_required
def notifications(request):
    return render(request, 'notifications.html', {
        'PageTitle': " - Notifications",
        'who_to_follows': who_to_follow(request),
        'recom_movies': movies_recommended(request),
        'popular_movies': popular_movies(request),
        'chat_users': accounts.views.followings(request.user)
    })


def movies_recommended(request):
    recommended_movies = []

    for top_movie in Movie.objects.filter(movierating__rate__gte=4.5, movierating__username_id=request.user.id):
        top_voters = CustomUser.objects.filter(movierating__rate__gte=4.5)
        for top_voter in top_voters:
            voters_top_movies = Movie.objects.filter(movierating__rate__gte=4.5, movierating__username_id=top_voter.id)
            for voters_top_movie in voters_top_movies:
                if not recommended_movies.__contains__(voters_top_movie):
                    recommended_movies.append(voters_top_movie)
    return recommended_movies


def who_to_follow(request):
    recommended_followings = []
    followings = []

    for following in Follow.objects.filter(follower_id=request.user.id):
        followings += CustomUser.objects.filter(id=following.following_id)
    for following in followings:
        f_followings = Follow.objects.filter(follower_id=following.id)
        for f_following in f_followings:
            if f_following.following_id != request.user.id:
                if not recommended_followings.__contains__(CustomUser.objects.get(id=f_following.following_id)):
                    recommended_followings.append(CustomUser.objects.get(id=f_following.following_id))
    for following in Follow.objects.filter(follower_id=request.user.id):
        if recommended_followings.__contains__(CustomUser.objects.get(id=following.following_id)):
            recommended_followings.remove(CustomUser.objects.get(id=following.following_id))

    return recommended_followings


def popular_movies(request):
    top_movies = []
    for repetitive_top_movie in Movie.objects.filter(movierating__rate__gte=4.8):
        if not top_movies.__contains__(repetitive_top_movie):
            top_movies.append(repetitive_top_movie)

    return top_movies