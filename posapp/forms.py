#from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Products

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


# class EmployeeForm(ModelForm):
#     class Meta:
#         model = Employee
#         fields = '__all__'
#         labels = {
#             'emp_id': '',
#             'emp_name': '',
#             'emp_pay_rate': '',
#             'emp_weekly_hours': '',
#             'emp_start_date': '',
#             'emp_dob': '',
#             'emp_email': '',
#         }

#         widgets = {
#             'emp_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee ID'}),
#             'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee Name'}),
#             'emp_pay_rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pay Rate'}),
#             'emp_weekly_hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Weekly Hours'}),
#             'emp_start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start Date'}),
#             'emp_dob': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
#             'emp_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
#         }


class CustomerForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
         

        
class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        labels = {
            'product_id': '',
            'product_name': '',
            'price': '',
            'category': '',
            'prod_amount': '',
            'instock': '',
         }

        widgets = {
            'product_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product ID: 0000-9999'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price: 00.00 - 1000.00'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'prod_amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'instock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Instock: 1 if yes, 0 if no'}),
            
         }


class EmployeeForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    is_staff = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2','is_staff']



class CategoryForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        labels = {
            'id': '',
            'name': '',
            'description': '',
            'status': '',
            'dateadded': '',
         }

        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product ID: 0000-9999'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price: 00.00 - 1000.00'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'dateadded': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
         }