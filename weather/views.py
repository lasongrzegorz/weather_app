from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index_view(request):

	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	cities = City.objects.all()
	weather_data = []

	for city in cities:
		json_weather_data = requests.get(
			'http://api.openweathermap.org/data/2.5/weather',
			params={
				'q': city,
				'units': 'metric',
				'appid': '4576744f6ce4bd418fce13e3b57ba1cf',
			},
		).json()

		city_weather = {
			'city': city.name,
			'temperature': json_weather_data['main']['temp'],
			'description': json_weather_data['weather'][0]['description'],
			'icon': json_weather_data['weather'][0]['icon'],
		}

		weather_data.append(city_weather)

	template = 'weather/weather.html'
	context = {
		'weather_data': weather_data,
		'form': form,
	}

	return render(request, template, context)

