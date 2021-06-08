from django.shortcuts import render, get_object_or_404, redirect
from ticketing.models import Movie, Cinema, ShowTime
# Create your views here.


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movie_list1_views': movies
    }
    return render(request, 'ticketing/movie_list.html', context)

def cinema_list(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinema_list1': cinemas
    }
    return render(request, 'ticketing/cinema_list.html', context)

def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie_views': movie
    }
    return render(request, 'ticketing/movie_details.html', context)

def cinema_details(request, cinema_id):
    cinema = get_object_or_404(Cinema,pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return render(request, 'ticketing/cinema_details.html', context)

def show_time(request):
    if request.user.is_authenticated:
        request.user.is_authenticated #making difference between logged in user and quests
        showtime = ShowTime.objects.all().order_by('start_time') #to sort scence based on time in show list page
        context = {
            'showtime_list_views':showtime
        }
        return render(request,'ticketing/showtime_list.html', context)
    else:
        return redirect('accounts:login') #if user is not logged in redirects to login page