from django.urls import path
from . import views
from .views import menuview, bookingview


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings', views.bookings, name='bookings'), 
    path('api/reservations', bookingview.as_view()), 
    path('api/menu-items', views.menuview.as_view()),
    path('api/items', views.Menuview.as_view()),
    path('api/items/<int:pk>', views.SingleMenuview.as_view()),
    path('api/access/', views.access),
]