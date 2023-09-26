from django.db import models

# Create your models here.
class CO2(models.Model):
    data = models.DateField()
    average = models.FloatField()

    class Meta:
        # Will be ordered from earlier to latest 
        ordering = ('date', )