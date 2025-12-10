from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release = models.DateField()
    country = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media/")
    genre = models.ManyToManyField(Genre, related_name="Movie")  # ← ManyToMany
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        default=1
    )

    def __str__(self):
        return self.title

    @property
    def review_count(self):
        return self.reviews.count()


class Review(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    film = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="Review")

    class Meta:
        permissions = [
            ("can_moderate_reviews", "Can moderate reviews"),
        ]

    def __str__(self):
        return f"Review by {self.name}"
