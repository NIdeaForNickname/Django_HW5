from django.urls import path
from . import views

app_name="firstapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_movie, name="add_movie"),
    path("<int:pk>/", views.movie_detail, name="movie_detail"),
    path('<int:pk>/edit/', views.edit_movie, name='edit_movie'),
    path('<int:pk>/delete/', views.delete_movie, name='delete_movie'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_review'),
]
