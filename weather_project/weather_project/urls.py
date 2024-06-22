"""
URL configuration for weather_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weather_app import views

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Home page URL
    path('', views.index, name='home'),

    # API endpoint for retrieving weather data for a specific city
    path('api/weather/<str:cityname>/', views.retrieve_city_weather, name='retrieve_city_weather'),

    # API endpoint for deleting a city from the database
    path('api/delete-city/<str:cityname>/', views.delete_city_api, name='delete_city_api'),
]
