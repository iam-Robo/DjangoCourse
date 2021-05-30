from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ticketing.models import Movie, Cinema


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movie_list1': movies
    }
    return render(request, 'ticketing/movie_list.html', context)

def cinema_list(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinema_list1': cinemas
    }
    return render(request, 'ticketing/cinema_list.html', context)