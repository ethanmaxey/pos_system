# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    category_id = models.ForeignKey(Category, models.DO_NOTHING)
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'


class Transactions(models.Model):
    id = models.IntegerField(primary_key=True)
    subtotal = models.CharField(max_length=45)
    grandtotal = models.CharField(max_length=45)
    tax = models.CharField(max_length=45)
    dateadded = models.CharField(max_length=45)
    empid = models.IntegerField()
    cusid = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='cusid')
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'transactions'


class Vendor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    address = models.TextField(blank=True, null=True)
    category_id = models.BigIntegerField()
    needorder = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'vendor'


class VendorCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendorid = models.ForeignKey(Vendor, models.DO_NOTHING, db_column='vendorid')
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='categoryid')

    class Meta:
        managed = False
        db_table = 'vendor_category'
