from django.urls import path, include
from weather.api import views
from rest_framework import routers


app_name = 'api'

router = routers.DefaultRouter()
router.register('city', views.CityView)

urlpatterns = [
    path('weather/', views.WeatherList.as_view(), name="weather_list"),
    path('city/', include(router.urls)),
]
