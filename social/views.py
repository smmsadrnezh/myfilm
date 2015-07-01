import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from accounts.models import CustomUser

from accounts.models import Follow
from social.models import Comment
from accounts.models import User
from myfilm.models import Movie
from social.models import Post
from social.models import Like
from social.models import MovieRating
from social.models import Notification
import accounts.views
import social.views


def post(request, postid):
    # get post likes
    likers = []
    for like in Like.objects.filter(post_id=postid):
        likers.append(User.objects.get(id=like.username_id))

    # get post comments
    comments_dic = {}
    for comment in Comment.objects.filter(post_id=postid):
        writer = User.objects.get(id=comment.username_id)
        comments_dic[comment] = writer
    return render(request, 'post.html', {
        'PageTitle': " - Post",
        'writer': CustomUser.objects.get(id=Post.objects.get(id=postid).username_id),
        'post': Post.objects.get(id=postid),
        'movie': Movie.objects.get(id=Post.objects.get(id=postid).movie_id),
        'likers': likers,
        'comments': comments_dic,
        'who_to_follows': who_to_follow(request),
        'recom_movies': movies_recommended(request),
        'popular_movies': popular_movies(request),
        'chat_users': accounts.views.followings(request.user),
        'notifications': social.views.notification_get(request.user.id),
        'secondLoad': 'like.html',
        'thirdLoad': 'comment.html'
    })


@login_required
def post_comment(request, postid):
    # add comment notification
    notification_add("comment", request.user,
                     CustomUser.objects.get(id=Post.objects.get(id=postid).username_id),
                     Post.objects.get(id=postid))
    if Comment.objects.filter(post_id=postid):
        for comment in Comment.objects.filter(post_id=postid):
            notification_add("comment_on_following", request.user,
                             CustomUser.objects.get(id=comment.username_id), Post.objects.get(id=postid))

    # add new comment
    Comment(body=request.POST['body'], post_id=postid, username_id=request.user.id,
            time=datetime.datetime.now(),
            title=request.POST['title']).save()

    comments_dic = {}
    for comment in Comment.objects.filter(post_id=postid):
        writer = User.objects.get(id=comment.username_id)
        comments_dic[comment] = writer
    return HttpResponse(render(request, 'comment.html', {
        'comments': comments_dic,
    }))


def post_like(request, postid):
    if request.is_ajax():
        if Like.objects.filter(post_id=postid, username_id=request.user.id):

            Like.objects.get(post_id=postid, username_id=request.user.id).delete()
        else:
            Like(post_id=postid, username_id=request.user.id, time=datetime.datetime.now()).save()
            notification_add("like", request.user, CustomUser.objects.get(id=Post.objects.get(id=postid).username_id),
                             Post.objects.get(id=postid))
        likers = []
        for like in Like.objects.filter(post_id=postid):
            likers.append(User.objects.get(id=like.username_id))

    return HttpResponse(render(request, 'like.html', {
        'likers': likers,
    }))


@login_required
def timeline_home(request):
    return render(request, 'timeline.html', {
        'PageTitle': " - Timeline",
        'posts': post_render(request)[0:1],
        'current_user': request.user,
        'who_to_follows': who_to_follow(request),
        'recom_movies': movies_recommended(request),
        'popular_movies': popular_movies(request),
        'chat_users': accounts.views.followings(request.user),
        'notifications': notification_get(request.user.id),
        'firstLoad': 'entry.html',
    })


def insert_post(request, postnumber):
    return HttpResponse(render(request, 'entry.html', {
        'posts': post_render(request)[0:int(postnumber)],
    }))


def post_render(request):
    followings = Follow.objects.filter(follower_id=request.user.id)
    all_posts = []
    for following in followings:
        for post in Post.objects.filter(username_id=following.following_id).order_by('created_time'):
            movie = Movie.objects.get(id=post.movie_id)
            all_posts.append((post, movie, CustomUser.objects.get(id=following.following_id)))
    return all_posts


def movies_recommended(request):
    recommended_movies = []
    user_top_movies = set()
    for top_movie in Movie.objects.filter(movierating__username_id=request.user.id, movierating__rate__gt=4.5):
        user_top_movies.add(top_movie)
    for top_movie in user_top_movies:
        top_voters = CustomUser.objects.filter(movierating__rate__gt=4.5, movierating__movie_id=top_movie.id).exclude(
            id=request.user.id)
        for top_voter in top_voters:
            voters_top_movies = Movie.objects.filter(movierating__rate__gt=4.5,
                                                     movierating__username_id=top_voter.id).exclude(id=top_movie.id)
            for voters_top_movie in voters_top_movies:
                if not recommended_movies.__contains__(voters_top_movie) and (
                        not user_top_movies.__contains__(voters_top_movie)):
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


@login_required
def notifications(request):
    return render(request, 'notifications.html', {
        'PageTitle': " - Notifications",
        'who_to_follows': who_to_follow(request),
        'recom_movies': movies_recommended(request),
        'popular_movies': popular_movies(request),
        'chat_users': accounts.views.followings(request.user),
        'notifications': notification_get(request.user.id)
    })


def notification_add(kind, user, notification_user, post):
    if user == notification_user:
        return
    else:
        Notification(text=notification_text(kind, user), time=datetime.datetime.now(), username_id=notification_user.id,
                     url=notification_url(kind, user, post)).save()


def notification_text(kind, user):
    return {
        'follow': user.first_name + " " + user.last_name + " started to following you.",
        'like': user.first_name + " " + user.last_name + " likes your update.",
        'comment': user.first_name + " " + user.last_name + " commented on your update.",
        'comment_on_following': user.first_name + " " + user.last_name + " commented on post you are following.",
    }.get(kind)


def notification_url(kind, user, post):
    if post:
        return {
            'like': "/posts/" + str(post.id),
            'comment': "/posts/" + str(post.id),
            'comment_on_following': "/posts/" + str(post.id),
        }.get(kind)
    else:
        return {
            'follow': "/profile/" + user.username,
        }.get(kind)


def notification_get(id):
    try:
        return Notification.objects.filter(username_id=id).order_by('-time')
    except Notification.DoesNotExist:
        return None


def notification_delete(request, notifid):
    Notification.objects.get(id=notifid).delete()
    return HttpResponseRedirect('/notifications')


def add_rate(request, movietitle, rate):
    if request.is_ajax():
        if MovieRating.objects.filter(username_id=request.user.id, movie_id=Movie.objects.get(title=movietitle).id):
            MovieRating.objects.filter(username_id=request.user.id,
                                       movie_id=Movie.objects.get(title=movietitle).id).update(
                rate=rate
            )
        else:
            MovieRating(movie_id=Movie.objects.get(title=movietitle).id, username_id=request.user.id, rate=rate).save()