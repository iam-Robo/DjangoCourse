from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from ticketing.models import Movie, Cinema, ShowTime, Ticket
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
    showtime = ShowTime.objects.all().order_by('start_time') #to sort scence based on time in show list page
    context = {
        'showtime_list_views':showtime
    }
    return render(request,'ticketing/showtime_list.html', context)

@login_required #if user is not logged in redirects to login page,next redirect to page user came from
def ticket_list(request):
    tickets = Ticket.objects.filter(customer=request.user.profile).order_by('-order_time')
    context = {
        'tickets': tickets
    }
    return render(request, 'ticketing/ticket_list.html', context)

@login_required
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    context = {
        'ticket': ticket
    }
    return render(request, 'ticketing/ticket_details.html', context)

@login_required
def showtime_details(request, showtime_id):
    showtime = ShowTime.objects.get(pk=showtime_id)
    context = {'showtime_view': showtime}
    #validation to buy  ticket
    if request.method == 'POST': #فقط زمانی وارد بلاک زیر شود که درخواست post یعنی از سمت کاربر باشد
        try:
            seat_count = int(request.POST['seat_count'])
            assert showtime.status == ShowTime.SALE_OPEN, 'فروش بلیط به اتمام رسیده است'
            assert showtime.free_seats >= seat_count, 'تعداد صندلی های خالی کمتر از مقدار درخواستی می باشد'
            total_price = showtime.price*seat_count
            assert request.user.profile.spend(total_price), 'موجودی کافی نمی باشد'
            showtime.reserve_seat(seat_count)
            Ticket.objects.create(showtime=showtime, customer=request.user.profile, seat_count=seat_count)
            context['message'] = 'خرید بلیط با موفقیت انجام شد'
            #to read errors and retutn as string to show in showtime_details page to user
        except Exception as e:
            context['error'] = str(e)

    return render(request, 'ticketing/showtime_details.html', context)