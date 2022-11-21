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

## point_of_sale tables


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class Customer(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=79)
    dob = models.TextField()

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
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


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=100)
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()


class Employee(models.Model):
    emp_id = models.PositiveIntegerField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    emp_pay_rate = models.CharField(max_length=6)
    emp_weekly_hours = models.DecimalField(max_digits=3, decimal_places=1)
    emp_start_date = models.DateField()
    emp_dob = models.DateField()
    emp_email = models.CharField(max_length=254)
    emp_age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'employee'