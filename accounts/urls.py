from django.urls import path
from accounts import views

app_name = 'accounts'  #this will be used for creating links in html files

urlpatterns=[
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('profile/details/', views.profile_details, name='profile_details'),
path('payment/list', views.payment_list, name='payment_list'),
path('payment/create', views.payment_create, name='payment_create'),
path('profile/edit', views.profile_edit, name='profile_edit'),
]