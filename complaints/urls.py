from django.urls import path
from . import views

urlpatterns = [
    path('complaints/', views.my_complaints, name='my_complaints'),
    path('complaints/new/', views.file_complaint, name='file_complaint'),
    path('complaints/<int:pk>/edit/', views.edit_complaint, name='edit_complaint'),
    path('complaints/<int:pk>/delete/', views.delete_complaint, name='delete_complaint'),
]