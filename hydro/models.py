# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accommodation(models.Model):
    reg_fio = models.CharField(max_length=-1)
    pers_num = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    comments = models.CharField(max_length=-1)
    reg_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'accommodation'

