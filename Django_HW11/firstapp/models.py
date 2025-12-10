from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release = models.DateField()
    country = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media/")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="Genre")
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        default=1
    )

    def __str__(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField()
    film = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="Review")
    
    def __str__(self):
        return self.name
