from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    image_path = models.FilePathField()
    imdb_url = models.URLField()

    def __str__(self):
        return "%s" % (self.title)


class Artist(models.Model):
    name = models.CharField(primary_key=True,max_length=100)
    image_path = models.FilePathField()
    birth_date = models.DateField()
    biography = models.TextField()
    birth_place = models.CharField(max_length=30)

    def __str__(self):
        return "%s" % (self.name)


class Movie_Artist(models.Model):
    artist_name = models.ForeignKey(Artist)
    movie_id = models.ForeignKey(Movie)
    role = models.CharField(max_length=30)

    class Meta:
        unique_together = (("artist_name", "movie_id"),)

    def __str__(self):
        return "%s %s" % (self.artist_name, self.role)