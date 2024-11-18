# customers/urls.py

from django.urls import path
from .views import customers_view, request_status_view, request_form 
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='customers/login.html'), name='login'),
    path('', customers_view, name='customers'),  # Main view
    path('request_status/', request_status_view, name='request_status_view'),  
    path('request_form/', request_form, name='request_form'),
      ]