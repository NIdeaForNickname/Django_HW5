from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Movie
from .forms import MovieForm

def index(request):
    movies = Movie.objects.all()
    return render(request, "index.html", { "movies" : movies })

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movie_detail.html", { "movie" : movie })

def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("firstapp:index")
    else:
        form = MovieForm()

    return render(request, "add_movie.html", {"form": form})