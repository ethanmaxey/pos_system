from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import connections
from django.contrib.auth.models import User

# Create your models here.


# class Employee(models.Model):
#     emp_id = models.CharField('Employee ID', max_length=3)
#     emp_name = models.CharField('Employee Name', max_length=50)
#     emp_pay_rate = models.CharField('Pay Rate', max_length=6)
#     emp_weekly_hours = models.DecimalField(
#         'Weekly Hours', max_digits=3, decimal_places=1)
#     emp_start_date = models.DateField('Employee Start Date')
#     emp_dob = models.DateField('Date of Birth')
#     emp_email = models.EmailField('Email Address')


# class Customer(models.Model):
#     cust_id = models.CharField('Customer ID', max_length=3)
#     cust_name = models.CharField('Customer Name', max_length=50)
#     cust_email = models.EmailField('Email Address')
#     cust_dob = models.DateField("Customer's Date of Birth")


# class PosappProduct(models.Model):
#     product_id = models.IntegerField(primary_key=True)
#     product_name = models.CharField(max_length=45)
#     price = models.CharField(max_length=45)
#     vendor_id = models.CharField(max_length=45)
#     vendor_category = models.CharField(max_length=45)
#     prod_amount = models.IntegerField()
#     in_stock = models.CharField(max_length=45)

#     class Meta:
#         managed = False
#         db_table = 'posapp_product'


# # class Transactions(models.Model):
# #     trans_id = models.CharField('Customer ID', max_length=3)
# #     trans_cust_name = models.CharField('Customer Name', max_length=50)
# #     trans_emp_id = models.EmailField('Email Address')
# #     trans_date = models.DateField("Customer's Date of Birth")

##############################################################

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
    date_added = models.DateField()
    date_updated = models.DateField()

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
    applied = models.DateField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    date_added = models.DateField()
    date_updated = models.DateField()
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
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'transactions'


class Vendor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField(blank=True, null=True)
    category_id = models.BigIntegerField()

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
