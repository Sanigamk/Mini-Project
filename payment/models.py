from django.db import models
from user.models import User
from slots.models import Slots
from booking.models import Booking
# Create your models here.
class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # slot_id = models.IntegerField()
    slot=models.ForeignKey(Slots,on_delete=models.CASCADE)
    card_holder_name = models.CharField(max_length=45)
    cvv = models.CharField(max_length=45)
    date = models.DateField()
    amount = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    # booking_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'
