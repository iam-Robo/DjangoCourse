from django.urls import path
from accounts import views

app_name = 'accounts'  #this will be used for creating links in html files

urlpatterns=[
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout')
]