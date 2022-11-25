# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    category_id = models.ForeignKey('Category', models.DO_NOTHING)
    amount = models.IntegerField()
    image = models.TextField(blank=True, null=True)
    vendor_id = models.ForeignKey('Vendor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products'
