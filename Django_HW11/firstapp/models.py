from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release = models.DateField()
    country = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media/")
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        default=1
    )

    def __str__(self):
        return self.title