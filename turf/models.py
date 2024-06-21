from django.db import models
from category.models import Category
from manager.models import Manager

# Create your models here.
class Turf(models.Model):
    turf_id = models.AutoField(primary_key=True)
    turfname = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    image = models.CharField(max_length=45)
    # category_id = models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # manager_id = models.IntegerField()
    manager=models.ForeignKey(Manager,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'turf'
