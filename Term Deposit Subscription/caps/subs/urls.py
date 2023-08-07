from django.urls import path
from . import views

app_name = 'subs'  # Set the app name

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
]
