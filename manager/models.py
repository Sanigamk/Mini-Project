from django.db import models

# Create your models here.
class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    contact = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    company_name = models.CharField(max_length=45)
    liscence_no = models.CharField(max_length=45)
    proof = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'manager'

