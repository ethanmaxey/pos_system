from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .forms import CustomerForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm

from .models import Customer, Employee, Products, AuthUser
from django.template import loader
from django.urls import reverse
#from posapp.models import Employee

# from POS.models import Departments, Employees
# from POS.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

# Renders html code
# def index(request):
#     return render(request, 'base.html')

# Tylers part below

@login_required(login_url='/login')
def home(request):
    # Pay Rate Pie Chart
    labels = []
    data = []

    queryset = Employee.objects.order_by('-emp_pay_rate')[:5]
    for emp in queryset:
        labels.append(emp.emp_name)
        data.append(emp.emp_pay_rate)

    return render(request, 'home.html', {
        'labels': labels,
        'data': data,
    })


@login_required
def EmpHome(request):
    return render(request, 'EmpHome.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

@login_required
def add_emp(request):
    form = EmployeeForm
    submitted = False

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/empTable')
    else:
        form = EmployeeForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'employee.html', {'form': form, 'submitted': submitted})

@login_required
def add_customer(request):
    form = CustomerForm
    submitted = False

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('custTable')
    else:
        form = CustomerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'customer.html', {'form': form, 'submitted': submitted})

@login_required
def add_product(request):
    form = ProductForm
    submitted = False
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_product')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'products.html', {'form': form, 'submitted': submitted})
    

@login_required
def custLand(request):
    return render(request, 'CustomerReport/CustomerLanding.html')

# def adminEmp(request):
#     return render(request, 'AdminReport/AdminEmployee.html')

@login_required
def adminVend(request):
    return render(request, 'AdminReport/AdminVendor.html')

@login_required
def empTrans(request):
    return render(request, 'EmployeeReport/EmployeeTransactions.html')

@login_required
def custRep(request):
    return render(request, 'EmployeeReport/EmployeeTransactions.html')


# IDK why but when these next two methods get removed the dashboard no longer works
@login_required
def shop(request):
    return render(request, 'shop.html')

@login_required
def cart(request):
    return render(request, 'shopping.html')

@login_required
def custTrans(request):
    return render(request, 'CustomerReport/CustomerLanding.html')

@login_required
def empTable(request):
    mydata = AuthUser.objects.all()
    template = loader.get_template('AdminReport/AdminEmployee.html')
    context = {
        'employees': mydata,
    }
    return HttpResponse(template.render(context, request))

@login_required
def custTable(request):
    mydata = AuthUser.objects.all()
    template = loader.get_template('CustomerReport/CustomerLanding.html')
    context = {
        'auth_user': mydata,
    }
    return HttpResponse(template.render(context, request))


@login_required
def prodTable(request):
    mydata = Products.objects.all()
    template = loader.get_template('Items.html')
    context = {
        'products': mydata,
    }
    return HttpResponse(template.render(context, request))


#   This is delete customer
@login_required
def delete(request, id):
    # Changed .get to .filter in order to remove the three john cena's
    member = Customer.objects.filter(cust_id=id)
    member.delete()
    return HttpResponseRedirect(reverse('custTable'))

@login_required
def deleteEmp(request, id):
    member = AuthUser.objects.filter(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('empTable'))


@login_required
def deleteProduct(request, id):
    member = Products.objects.get(product_id=id)
    member.delete()
    return HttpResponseRedirect(reverse('prodTable'))


# @login_required
# def transactionTable(request):
#     mydata = Transactions.objects.all()
#     template = loader.get_template('templates\Items.html')
#     context = {
#         'products': mydata,
#     }
#     return HttpResponse(template.render(context, request))

@login_required
def transactionTable(request):
    return render(request, 'transactions.html')