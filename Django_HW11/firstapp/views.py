from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime

# Create your views here.
from .models import Movie, Review
from .forms import MovieForm, ReviewForm

def index(request):
    sort = request.GET.get('sort')

    if sort == 'rating':
        movies = Movie.objects.all().order_by('-rating')
    elif sort == 'date':
        movies = Movie.objects.all().order_by('-release')
    else:
        movies = Movie.objects.all()

    return render(request, 'index.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            mname = form.cleaned_data["name"] + f"{movie.Review.count()}" 
            mdate = datetime.now()
            mtext = form.cleaned_data["text"]

            a = Review(name=mname, date=mdate, text=mtext, film=movie)
            a.save()
            return redirect("firstapp:movie_detail", pk=pk)
    
    form = ReviewForm()
    return render(request, "movie_detail.html", { "form": form, "movie" : movie, "reviews": movie.Review.all(), "Genres": movie.genre.all()})

def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("firstapp:index")
    else:
        form = MovieForm()

    return render(request, "add_movie.html", {"form": form})

def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('firstapp:movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)

    return render(request, 'edit_movie.html', {'form': form, 'movie': movie})


def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('firstapp:index')
    return render(request, 'delete_movie.html', {'movie': movie})

def delete_comment(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect("firstapp:index")
    return render(request, "delete_review.html", {"review": review})