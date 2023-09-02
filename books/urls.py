from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('search/', views.search_books, name='search_books'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('request_exchange/<int:pk>/', views.request_exchange, name='request_exchange'),
    path('view_exchange_requests/', views.view_exchange_requests, name='view_exchange_requests'),
]
