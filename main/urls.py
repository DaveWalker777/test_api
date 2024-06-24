from django.urls import path
from . import views

urlpatterns = [
    path('api/ad/<int:pk>/', views.ad_detail, name='ad-detail'),
    path('api/ad/', views.ad_list, name='ad-list'),
    path('', views.ads_list, name='ads-list'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
]
