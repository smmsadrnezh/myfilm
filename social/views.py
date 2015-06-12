from django.http import HttpResponseRedirect
from django.shortcuts import render

from accounts.models import CustomUser
from social.models import MovieRating
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
            'current_user': request.user
        })


def timeline_home(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        followings = Follow.objects.filter(follower_id=request.user.id)
        all_posts = []
        for following in followings:
            posts = Post.objects.filter(username_id=following.following_id)
            writer = CustomUser.objects.filter(id=following.following_id)[0]
            for post in posts:
                movie = Movie.objects.filter(id=post.movie_id)[0]
                all_posts.append((post, movie, writer))

        return render(request, 'timeline.html', {
            'PageTitle': "Myfilm - Timeline",
            'posts': all_posts,
            'current_user': request.user
        })


def notifications(request):
    if request.user.id == None:
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'notifications.html', {
            'PageTitle': "Notifications",
            'current_user': request.user
        })


def movie_recommended(request):
    return


def who_to_follw(request):
    return


def popular_movies(request):
    top_movies = MovieRating.objects.filter(rate__gte=4.8)
    return top_movies