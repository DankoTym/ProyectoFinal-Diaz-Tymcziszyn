from django.urls import path
from AppSuper import views

urlpatterns = [
    path('', views.Inicio, name="inicio"),
]
