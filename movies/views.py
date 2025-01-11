from .models import Movie
from django.shortcuts import render

def movie_list(request):
    movies = Movie.objects.all() 
    return render(request, 'index.html', {'movies': movies})
def add_movie(request):
    return render(request, 'movies/add_movies')