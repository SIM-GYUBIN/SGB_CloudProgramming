from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.main, name='main'),
    path('delete/<str:city_id>/', views.delete_city, name='delete_city'),
]