from rest_framework import serializers
from weather.models import Weather, City


class WeatherSerializer(serializers.ModelSerializer):

	class Meta:
		model = Weather
		fields = [
			'city',
			'temperature',
			'description',
			'icon',
		]


class CitySerializer(serializers.ModelSerializer):

	class Meta:
		model = City
		fields = [
			'name',
		]