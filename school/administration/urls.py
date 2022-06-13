from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('Admission_office/',views.Admission_office, name = "Admission_office"),
]