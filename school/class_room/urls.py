from django.urls import path
from . import views

urlpatterns = [
    path('', views.Exam_number),
    path('login/', views.login_forms , name="login"),
    
]