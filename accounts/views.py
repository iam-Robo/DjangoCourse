from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse


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