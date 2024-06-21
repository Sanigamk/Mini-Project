from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.CharField(max_length=45)
    house_name = models.CharField(max_length=45)
    post = models.CharField(max_length=45)
    pin = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    phn_no = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'user'

