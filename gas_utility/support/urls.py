from django.urls import path
from . import views  # Make sure to import your views

urlpatterns = [
    path('', views.support_home, name='support_home'),  # This will match /support/
    path('requests/', views.request_list, name='request_list'),
    path('requests/<int:pk>/', views.request_detail, name='request_detail'),
]