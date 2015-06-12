from django.shortcuts import render
from social.models import Post
from accounts.models import User
from myfilm.models import Movie
from social.models import Like
from social.models import Comment
from accounts.models import CustomUser
from social.models import MovieRating

def post(request, postid):
    post = Post.objects.filter(id=postid)
    if len(post)>0:
        post = post[0]

    writer = User.objects.filter(id=post.username_id)
    if len(writer)>0:
        writer = writer[0]
    cwriter = CustomUser.objects.filter(user_ptr_id = writer.id)[0]

    movie = Movie.objects.filter(id=post.movie_id)
    if len(movie)>0:
        movie = movie[0]

    likes = Like.objects.filter(post_id=postid)
    likers = []
    if(len(likes)>0):
        for like in likes:
            likers.append(User.objects.filter(id=like.username_id)[0])

    comments = Comment.objects.filter(post_id=postid)
    comments_dic = {}
    for comment in comments:
        writer = User.objects.filter(id=comment.username_id)[0]
        comments_dic[comment] = writer

    return render(request, 'post.html', {
        'PageTitle': "Post",
        'cwriter':cwriter,
        'writer': writer,
        'post': post,
        'movie': movie,
        'likers': likers,
        'comments': comments_dic
    })


def timeline_home(request):
    return render(request, 'timeline.html', {
        'PageTitle': "Myfilm - Timeline",
    })


def notifications(request):
    return render(request, 'notifications.html', {
        'PageTitle': "Notifications",
    })

def movie_recommended(request):
    return

def who_to_follw(request):
    return

def popular_movies(request):
    top_movies = MovieRating.objects.filter(rate__gte=4.8)
    return top_movies

