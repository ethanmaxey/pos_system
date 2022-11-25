#from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Products, Category, Vendor

class DateInput(forms.DateInput):
    input_type = 'date'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


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
    # username = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    is_staff = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2','is_staff']



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = 'name', 'description', 'date_added'#, 'date_updated'
        labels = {
            'name': '',
            'description': '',
            'date_added': '',
            # 'date_updated': '',
         }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'date_added': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Added'})
            # 'date_updated': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Added'})
         }



class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields =  'id', 'name', 'address', 'category_id'#, 'needorder'
        labels = {
            'id': '',
            'name': '',
            'address': '',
            'category_id': '',
            # 'needorder': ''
         }

        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'category_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category ID'}),
            # 'needorder': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Need Order?: Yes/No'})
         }

