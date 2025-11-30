from django.urls import path
from . import views

app_name="firstapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_movie, name="add_movie"),
    path("<int:pk>/", views.movie_detail, name="movie_detail")
]
