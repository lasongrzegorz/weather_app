from django.db import models


class City(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'cities'


def get_sentinel_city():
	return City.objects.get_or_create(name='deleted')


class Weather(models.Model):
	city = models.ForeignKey(City, on_delete=models.SET(get_sentinel_city))
	temperature = models.FloatField(null=True, blank=True)
	description = models.CharField(max_length=100, null=True, blank=True)
	icon = models.CharField(max_length=64, null=True, blank=True)
	updated = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return f'{self.city} weather on {"{:%Y-%m-%d}".format(self.updated)}'
