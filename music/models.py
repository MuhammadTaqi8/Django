from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    albumTitle = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    albumLogo = models.CharField(max_length=250)
    def __str__(self):
        return self.albumTitle + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE) 
    fileType = models.CharField(max_length=250)
    songTitle = models.CharField(max_length=250)
    def __str__(self):
        return self.songTitle
    