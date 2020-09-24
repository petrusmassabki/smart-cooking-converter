from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resultado/', views.result, name='result'),
    path('dados/', views.data, name='data'),
]