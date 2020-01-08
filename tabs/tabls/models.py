from django.db import models

# Create your models here.
class hubinfo(models.Model):
    hub_id = models.IntegerField(PRIMA)
    latitude = models.DecimalField(decimal_places=2)
    longitude = models.DecimalField(decimal_places=2)

class logs(models.Model):
    timestamp
