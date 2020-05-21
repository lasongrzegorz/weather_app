from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
import requests
from .models import City
from .forms import CityForm
from django.views.generic import DeleteView


def index_view(request):

	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	cities = City.objects.all()
	weather_data = []
	for city in cities:
		city_weather_url = requests.get(
			'http://api.openweathermap.org/data/2.5/weather',
			params={
				'q': city,
				'units': 'metric',
				'appid': '4576744f6ce4bd418fce13e3b57ba1cf',
			},
		)

		if city_weather_url.status_code == 200:
			city_weather_data = city_weather_url.json()
			city_weather = {
				'city': city.name,
				'temperature': city_weather_data['main']['temp'],
				'description': city_weather_data['weather'][0]['description'],
				'icon': city_weather_data['weather'][0]['icon'],
				'city_db_id': city.id,
			}
			weather_data.append(city_weather)
		else:
			warning_message = f"City '{city}' has not been found."
			messages.add_message(request, messages.WARNING, warning_message)
			City.objects.get(id=city.id).delete()

	template = 'weather/weather.html'
	context = {
		'weather_data': weather_data,
		'form': form,
	}

	return render(request, template, context)


class DeleteCityView(DeleteView):
	model = City
	pk_url_kwarg = 'city_id'
	success_url = reverse_lazy('weather:index')
