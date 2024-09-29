from django.urls import path 
from first_app import views
# from first_app.views import home

urlpatterns = [
    path('', views.home),
]
