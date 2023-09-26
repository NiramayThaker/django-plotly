from django.db import models


# Create your models here.
class CO2(models.Model):
	date = models.DateField()
	average = models.FloatField()

	class Meta:
		# Will be ordered from earlier to latest
		ordering = ('date',)

	def __str__(self):
		return f"{self.date}"
