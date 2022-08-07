


from django.db import models

class Beach_List(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    class Meta:
        db_table = 'beach_list'
        managed = False
