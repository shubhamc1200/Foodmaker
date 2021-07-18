from django.db import models

# Create your models here.
class Lat_Long(models.Model):
    name=models.CharField(max_length=100,default="No name")
    latitude = models.FloatField(null=True)
    longitude= models.FloatField(null=True);
    def __str__(self):
        return str(self.latitude)+', '+str(self.longitude)
