from django.urls import path
from . import views

urlpatterns = [
    path('', views.holiday_ss, name='holiday_ss'),
    path('hello', views.hello, name='hello'),
    path('api', views.api, name='api'),
]