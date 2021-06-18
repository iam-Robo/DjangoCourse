from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from ticketing.models import Movie, Cinema, ShowTime, Ticket
from ticketing.forms import ShowTimeSearchForm

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
    search_form = ShowTimeSearchForm(request.GET)
    showtime = ShowTime.objects.all().order_by('start_time')  # to sort scence based on time in show list page
    if search_form.is_valid():
        showtime = showtime.filter(movie__name__contains=search_form.cleaned_data['movie_name'])
        if search_form.cleaned_data['sale_is_open']:
            showtime = showtime.filter(status=ShowTime.SALE_OPEN)
        if search_form.cleaned_data['movie_min_length'] is not None:
            showtime = showtime.filter(movie__length__gte=search_form.cleaned_data['movie_min_length'])
        if search_form.cleaned_data['movie_max_length'] is not None: #to prevent non error on making query
            showtime = showtime.filter(movie__length__lte=search_form.cleaned_data['movie_max_length'])
        if search_form.cleaned_data['cinema'] is not None:
            showtime = showtime.filter(cinema__name=search_form.cleaned_data['cinema'])

        min_price, max_price = search_form.price_levels()
        if min_price is not None:
            showtime = showtime.filter(price__gte=min_price)
        if max_price is not None:
            showtime = showtime.filter(price__lte=max_price)

    showtime = showtime.order_by('start_time')
    context = {
        'showtime_list_views': showtime,
        'search_form': search_form,
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