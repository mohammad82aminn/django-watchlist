from django.http import HttpResponse
from django.shortcuts import render

from movie.models import Movie

def movies_list_view(request):
    movies = Movie.objects.all()
    context = {
        "movies_list": movies,
    }
    return render(request, "movie/movies_list.html", context)
# Create your views here.
