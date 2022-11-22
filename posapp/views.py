from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .forms import CustomerForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm,ProductForm, CategoryForm
import random
from .models import Products, AuthUser, Transactions, Category
from django.template import loader
from django.urls import reverse

# from cart.cart import Cart

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
    labels2 = []
    data2 = []

    queryset =Products.objects.order_by('-price')[:5]
    for prod in queryset:
        labels.append(prod.name)
        data.append(prod.price)

    queryset2 = AuthUser.objects.order_by('-is_active')[:5]
    for emp in queryset2:
        if emp.is_staff == 1:
            labels2.append(emp.first_name)
            a = emp.is_active * random.randint(1, 10) * 1000
            data2.append(a) 

    return render(request, 'home.html', {
        'labels': labels,
        'data': data,
        'labels2': labels2,
        'data2': data2,
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
    form = RegisterForm()
    submitted = False

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/custTable')
    else:
        form = RegisterForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'customer.html', {'form': form, 'submitted': submitted})

@login_required
def add_product(request):
    form =ProductForm
    submitted = False
    
    if request.method == 'POST':
        form =ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/prodTable')
    else:
        form =ProductForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'products.html', {'form': form, 'submitted': submitted})


@login_required
def add_category(request):
    form =CategoryForm()
    submitted = False
    
    if request.method == 'POST':
        form =CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/catTable')
    else:
        form =CategoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'categoryadd.html', {'form': form, 'submitted': submitted})
    

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
    mydata =Products.objects.all()
    template = loader.get_template('shop.html')
    context = {
        'products': mydata,
    }
    return HttpResponse(template.render(context, request))



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
    mydata =Products.objects.all()
    template = loader.get_template('Items.html')
    context = {
        'products': mydata,
    }
    return HttpResponse(template.render(context, request))


@login_required
def catTable(request):
    mydata = Category.objects.all()
    template = loader.get_template('category.html')
    context = {
        'category': mydata,
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
def deleteCust(request, id):
    member = AuthUser.objects.filter(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('custTable'))


@login_required
def deleteProduct(request, id):
    member =Products.objects.get(id=id)
    member.delete()
    context = {
        'products': member,
    }
    return HttpResponseRedirect(reverse('prodTable'))


@login_required
def deleteCategory(request, id):
    member =Category.objects.get(id=id)
    member.delete()
    context = {
        'category': member,
    }
    return HttpResponseRedirect(reverse('catTable'))


# @login_required
# def transactionTable(request):
#     mydata = Transactions.objects.all()
#     template = loader.get_template('templates\Items.html')
#     context = {
#         'productsproductss': mydata,
#     }
#     return HttpResponse(template.render(context, request))

@login_required
def transactionTable(request):
    mydata = Transactions.objects.all()
    template = loader.get_template('transactions.html')
    context = {
        'transaction': mydata,
    }
    return HttpResponse(template.render(context, request))






#IAN'S CODE
#this is the cart section

#Cart is not defined in pylance
@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    products = products.objects.get(id=id)
    cart.add(productsproducts=productsproducts)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    products =products.objects.get(id=id)
    cart.remove(productsproducts)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    products =products.objects.get(id=id)
    cart.add(productsproducts=productsproducts)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    products =products.objects.get(id=id)
    cart.decrement(productsproducts=productsproducts)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')