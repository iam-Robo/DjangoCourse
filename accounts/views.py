from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from accounts.forms import PaymentForm
from accounts.models import Payment


# Create your views here.



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'کاربری با مشخصات وارد شده یافت نشد')
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            return HttpResponseRedirect(reverse('ticketing:showtime_list')) #after login redirects to showtime list

    else:
        if request.user.is_authenticated: #if user is allready logged in
            return HttpResponseRedirect(reverse('ticketing:showtime_list'))
        else:
            return render(request, 'accounts/login.html', {})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

@login_required
def profile_details(request):
    profile = request.user.profile #for one to on key
    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile_details.html', context)

@login_required()
def payment_list(request):
    payment = Payment.objects.filter(profile=request.user.profile).order_by('-transaction_time')
    context = {
        'payment_list_views': payment
    }
    return render(request, 'accounts/payment_list.html', context)

@login_required()
def payment_create(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)   #commit=False means to not Save the data
            request.user.profile.deposit(payment.amount)    #to save amount into user deposit amount
            payment.profile = request.user.profile   #to set profile to current user
            payment_form.save()
            return HttpResponseRedirect(reverse('accounts:payment_list'))
    else:
        payment_form = PaymentForm()
    context = {
        'payment_form_view': payment_form
    }
    return render(request, 'accounts/payment_create.html', context)
