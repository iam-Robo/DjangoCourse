from django.contrib.auth import authenticate, login
from django.shortcuts import render, Http404, HttpResponse

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise Http404('نام کاربری یا رمز اشتباه است')
        else:
            login(request,user)
            return HttpResponse('ماشالاح')

    else:
        return render(request, 'accounts/login.html', {})

def logout_view(request):
    pass