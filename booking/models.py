from django.db import models
from user.models import User
from slots.models import Slots
from turf.models import Turf
from category.models import Category
# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # slot_id = models.IntegerField()
    slot=models.ForeignKey(Slots,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=45)
    # turf_id = models.IntegerField()
    # turf=models.ForeignKey(Turf,on_delete=models.CASCADE)
    # pay_status = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'booking'
