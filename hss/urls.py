from django.urls import path
from . import views

urlpatterns = [
    path('', views.holiday_ss, name='holiday_ss'),
]