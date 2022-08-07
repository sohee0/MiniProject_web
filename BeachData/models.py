from django.db import models

# Create your models here.

class Wave(models.Model):
    obs_time = models.CharField(max_length=50, null=True)
    air_temp = models.FloatField(null=True)
    water_temp = models.FloatField(null=True)
    wind_speed = models.FloatField(null=True)
    wind_direct = models.CharField(max_length=50, null=True)
    wave_height = models.FloatField(null=True)
    wave_period = models.FloatField(null=True)
    score = models.IntegerField(null=True)
    score_msg = models.CharField(max_length=50, null=True)
    beach_name = models.CharField(max_length=50, null=True)

    class Meta:
      db_table = 'wave'
      ordering = ['-id', 'obs_time', 'air_temp', 'water_temp', 'wind_speed', 'wind_direct', 'wave_height', 'wave_period', 'score', 'score_msg', 'beach_name']
      managed = False