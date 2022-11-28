# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Transactions(models.Model):
    subtotal = models.CharField(max_length=45)
    grandtotal = models.CharField(max_length=45)
    tax = models.CharField(max_length=45)
    dateadded = models.CharField(max_length=45)
    empid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='empid')
    category = models.ForeignKey('Category', models.DO_NOTHING)
    custid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'
