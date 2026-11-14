from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
    path('dashboard/resident/', views.resident_dashboard, name='resident_dashboard'),
    path('dashboard/tanod/', views.tanod_dashboard, name='tanod_dashboard'),
    path('dashboard/official/', views.official_dashboard, name='official_dashboard'),
    path('dashboard/official/approve/<int:user_id>/', views.approve_staff, name='approve_staff'),
]