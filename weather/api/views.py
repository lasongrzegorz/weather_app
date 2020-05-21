from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from weather.models import Weather, City
from .serializers import WeatherSerializer, CitySerializer


class WeatherList(APIView):

	def get(self, request):
		weather = Weather.objects.all()
		serializer = WeatherSerializer(weather, many=True)
		return Response(serializer.data)


class CityView(viewsets.ModelViewSet):
	queryset = City.objects.all()
	serializer_class = CitySerializer
