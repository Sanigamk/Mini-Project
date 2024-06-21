from django.db import models
from turf.models import Turf

# Create your models here.
class Slots(models.Model):
    slot_id = models.AutoField(primary_key=True)
    # turf_id = models.IntegerField()
    turf=models.ForeignKey(Turf,on_delete=models.CASCADE)
    start_time = models.CharField(max_length=45)
    end_time = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    price = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'slots'

