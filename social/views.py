from django.http import HttpResponseRedirect
from accounts.models import CustomUser
import accounts.views
from django.shortcuts import render
from accounts.models import Follow
from social.models import Comment
from accounts.models import User
from myfilm.models import Movie
from social.models import Post
from social.models import Like


def post(request, postid):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        post = Post.objects.filter(id=postid)
        if len(post) > 0:
            post = post[0]

        post_writer = CustomUser.objects.filter(id=post.username_id)
        if len(post_writer) > 0:
            post_writer = post_writer[0]

        movie = Movie.objects.filter(id=post.movie_id)
        if len(movie) > 0:
            movie = movie[0]

        likes = Like.objects.filter(post_id=postid)
        likers = []
        if (len(likes) > 0):
            for like in likes:
                likers.append(User.objects.filter(id=like.username_id)[0])

        comments = Comment.objects.filter(post_id=postid)
        comments_dic = {}
        for comment in comments:
            writer = User.objects.filter(id=comment.username_id)[0]
            comments_dic[comment] = writer

        return render(request, 'post.html', {
            'PageTitle': "Post",
            'writer': post_writer,
            'post': post,
            'movie': movie,
            'likers': likers,
            'comments': comments_dic,
            'current_user': request.user,
            'following_users': who_to_follw(request),
            'recom_movies': movies_recommended(request),
            'popular_movies': popular_movies(request),
            'chat_users': accounts.views.followings(request.user)
        })


def timeline_home(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        followings = Follow.objects.filter(follower_id=request.user.id)
        all_posts = []
        for following in followings:
            posts = Post.objects.filter(username_id=following.following_id).order_by('created_time')
            writer = CustomUser.objects.filter(id=following.following_id)[0]
            for post in posts:
                movie = Movie.objects.filter(id=post.movie_id)[0]
                all_posts.append((post, movie, writer))

        return render(request, 'timeline.html', {
            'PageTitle': "Myfilm - Timeline",
            'posts': all_posts,
            'current_user': request.user,
            'following_users': who_to_follw(request),
            'recom_movies': movies_recommended(request),
            'popular_movies': popular_movies(request),
            'chat_users': accounts.views.followings(request.user)
        })


def notifications(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'notifications.html', {
            'PageTitle': "Notifications",
            'current_user': request.user,
            'following_users': who_to_follw(request),
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


def who_to_follw(request):
    recommended_followings = []
    followings = []

    for following in Follow.objects.filter(follower_id=request.user.id):
        followings += CustomUser.objects.filter(id=following.following_id)
    for following in followings:
        f_followings = Follow.objects.filter(follower_id=following.id)
        for f_following in f_followings:
            if not recommended_followings.__contains__(CustomUser.objects.filter(id=f_following.following_id)[0]):
                recommended_followings.append(CustomUser.objects.filter(id=f_following.following_id)[0])

    return recommended_followings


def popular_movies(request):
    top_movies = []
    for repetitive_top_movie in Movie.objects.filter(movierating__rate__gte=4.8):
        if not top_movies.__contains__(repetitive_top_movie):
            top_movies.append(repetitive_top_movie)

    return top_movies