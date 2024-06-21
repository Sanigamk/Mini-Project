from django.db import models
from turf.models import Turf
from user.models import User

# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    # turf_id = models.IntegerField()
    turf=models.ForeignKey(Turf,on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'feedback'
