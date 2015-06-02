from django.db import models


class Movie:
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField()
    year = models.IntegerField()
    description = models.TextField()
    image_path = models.FilePathField()
    imdb_url = models.URLField()

    def __str__(self):
        return "%s" % (self.title)


class Artist:
    name = models.CharField(primary_key=True)
    image_path = models.FilePathField()
    birth_date = models.DateField()
    biography = models.TextField()
    birth_place = models.CharField()

    def __str__(self):
        return "%s" % (self.name)


class Movie_Artist:
    artist_name = models.ForeignKey(Artist, primary_key=True)
    movie_id = models.ForeignKey(Movie, primary_key=True)
    role = models.CharField()

    def __str__(self):
        return "%s %s" % (self.artist_name, self.role)