from django.urls import path
from . import views

urlpatterns = [
    path('webinterface/', views.webinterface, name='webinterface'),
]