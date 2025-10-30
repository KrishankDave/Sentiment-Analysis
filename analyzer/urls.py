"""
URL configuration for analyzer app
"""

from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Main application URLs
    path('', views.home, name='home'),
    path('analyze/', views.analyze_ajax, name='analyze_ajax'),
]

