from django.urls import path
from . import views


app_name = 'weather'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('delete/<int:city_id>', views.DeleteCityView.as_view(), name='delete'),
]
