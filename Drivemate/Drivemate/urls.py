"""Drivemate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from drivemate import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home,name='home'),
    path('login_view/', views.login_view, name='login_view'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('acservices/', views.acservices, name='acservices'),
    path('detailing/', views.detailing, name='detailing'),
    path('battery_services/', views.battery_services, name='battery_services'),
    path('add_to_cart/<str:product_name>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove_from_cart/<str:item_name>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('decrease_item_quantity/<str:item_name>/', views.decrease_item_quantity, name='decrease_item_quantity'),
    path('increase_item_quantity/<str:item_name>/', views.increase_item_quantity, name='increase_item_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('logout/', views.logout, name='logout'),
]