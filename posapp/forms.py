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
        fields = ['id', 'name', 'description', 'price', 'date_added', 'date_updated', 'category_id', 'amount', 'image', 'vendor_id']
        labels = {
            'id': '',
            'name': '',
            'description': '',
            'price': '',
            'date_added': '',
            'date_updated': '',
            'category_id': '',
            'amount': '',
            'image': '',
            'vendor_id': '',
         }

        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Product ID: 0000-9999'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price: 00.00 - 1000.00'}),
            'date_added': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Added'}),
            'date_updated': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Updated'}),
            'category_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Category ID'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'vendor_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Vendor ID'}),
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
        fields = 'name', 'description', 'date_added', 'date_updated'
        labels = {
            'name': '',
            'description': '',
            'date_added': '',
            'date_updated': '',
         }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'date_added': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Added'}),
            'date_updated': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Updated'})
         }



class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields =  'id', 'name', 'address', 'category_id', 'need_order'
        labels = {
            'id': '',
            'name': '',
            'address': '',
            'category_id': '',
            'need_order': ''
         }

        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor ID'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'category_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category ID'}),
            'need_order': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Need Order: True/False'})
         }



class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)