from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release = models.DateField()
    country = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.title