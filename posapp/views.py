from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .forms import CustomerForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm,ProductForm, CategoryForm, VendorForm
import random
from .models import Products, AuthUser, Transactions, Category, Vendor
from django.template import loader
from django.urls import reverse
from django.contrib import messages
import time
# from cart.cart import Cart

# Create your views here.

@login_required(login_url='/login')
def home(request):
    # Pay Rate Pie Chart
    labels = []
    data = []
    labels2 = []
    data2 = []
    labels1 = []
    data1 = []

    queryset =Products.objects.order_by('-price')[:5]
    for prod in queryset:
        labels.append(prod.name)
        data.append(prod.price)

    # queryset1 =Transactions.objects.order_by('-grandtotal')[:5]
    # for prod in queryset1:
    #     if user.id == queryset1.id:
    #         labels1.append(user.first_name)
    #         data1.append(prod.grandtotal)

    queryset2 = AuthUser.objects.order_by('-is_staff')[:10]
    for emp in queryset2:
        if emp.is_staff == 1:
            if emp.is_superuser == 0:
                labels2.append(emp.first_name)
                a = emp.is_active * random.randint(1, 10) * 1000
                data2.append(a) 

    return render(request, 'home.html', {
        'labels': labels,
        'data': data,
        'labels2': labels2,
        'data2': data2,
        'labels1': labels1,
        'data1': data1,
    })

@login_required
def one(request):
    return render(request, 'one.html')

@login_required
def two(request):
    return render(request, 'two.html')

@login_required
def three(request):
    return render(request, 'three.html')

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
def add_vendors(request):
    form = VendorForm()
    submitted = False
    
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vendTable')
    else:
        form = VendorForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'vendorAdd.html', {'form': form, 'submitted': submitted})
    

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
    return render(request, 'shop.html', {'products':mydata})

@login_required
def cart(request):
    return render(request, 'cart.html')

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


@login_required
def catTable(request):
    mydata = Category.objects.all()
    template = loader.get_template('category.html')
    context = {
        'category': mydata,
    }
    return HttpResponse(template.render(context, request))

@login_required
def vendTable(request):
    mydata =Vendor.objects.all()
    template = loader.get_template('vendor.html')
    context = {
        'vendors': mydata,
    }
    return HttpResponse(template.render(context, request))

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



@login_required
def deleteVendor(request, id):
    member =Vendor.objects.get(id=id)
    member.delete()
    context = {
        'vendors': member,
    }
    return HttpResponseRedirect(reverse('vendTable'))

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


@login_required
def updateEmp(request, id):

    employee = AuthUser.objects.get(id=id)
    template = loader.get_template('update_employee.html')
    context = {
        'up_employee': employee,
    }
    return HttpResponse(template.render(context, request))

@login_required()
def empSubmit(request, id):
  first = request.POST['first_name']
  last = request.POST['last_name']
  mail = request.POST['email']
  user = request.POST['username']
  member = AuthUser.objects.get(id=id)
  member.first_name = first
  member.last_name = last
  member.email = mail
  member.username = user
  member.save()
  return HttpResponseRedirect(reverse('empTable')) 


@login_required
def updateCust(request, id):
  mymember = AuthUser.objects.get(id=id)
  template = loader.get_template('update_customer.html')
  context = {
    'up_customer': mymember,
  }
  return HttpResponse(template.render(context, request))

@login_required()
def custSubmit(request, id):
  first = request.POST['first_name']
  last = request.POST['last_name']
  mail = request.POST['email']
  user = request.POST['username']
  member = AuthUser.objects.get(id=id)
  member.first_name = first
  member.last_name = last
  member.email = mail
  member.username = user
  member.save()
  return HttpResponseRedirect(reverse('custTable')) 


@login_required
def updateProd(request, id):
  mymember = Products.objects.get(id=id)
  template = loader.get_template('update_product.html')
  context = {
    'up_product': mymember,
  }
  if mymember.amount < 50:
      messages.info(request, 'Low on product, please order more!')
  
  return HttpResponse(template.render(context, request))

@login_required()
def prodSubmit(request, id):
  name = request.POST['name']
  description = request.POST['description']
  price = request.POST['price']
  dateupdated = request.POST['dateupdated']
  amount = request.POST['amount']
  
  
  member = Products.objects.get(id=id)
  member.name = name
  member.description = description
  member.price = price
  member.dateupdated = dateupdated
  member.amount = amount
  member.save()
  return HttpResponseRedirect(reverse('prodTable')) 


@login_required
def updateVendor(request, id):
    vendor = Vendor.objects.get(id=id)
    # vendor.id
    # vendor.category_id
    # vendor.need_order
    
    template = loader.get_template('update_vendor.html')
    context = {
        'up_vendor': vendor,
    }
    return HttpResponse(template.render(context, request))

@login_required()
def vendSubmit(request, id):
  name = request.POST['name']
  address = request.POST['address']
#   category_id = request.POST['category_id']
  need_order = request.POST['need_order']
  member = Vendor.objects.get(id=id)
  member.need_order = need_order
  member.name = name
  member.address = address
#   member.category_id = category_id
  member.save()
  return HttpResponseRedirect(reverse('vendTable'))

@login_required
def updateCategory(request, id):
  mymember = Category.objects.get(id=id)
  template = loader.get_template('update_category.html')
  context = {
    'up_category': mymember,
  }
  return HttpResponse(template.render(context, request))

@login_required()
def categorySubmit(request, id):
  id = request.POST['id']
  name = request.POST['name']
#   description = request.POST['description']
  date_updated = request.POST['date_updated']
  
  member = Category.objects.get(id=id)
  member.id = id
  member.name = name
#   member.description = description
  member.date_updated = date_updated
  
  member.save()
  return HttpResponseRedirect(reverse('catTable'))

def buyProd(request, id):
    product = Products.objects.get(id=id)
    
    var1 = product.amount
    product.amount = product.amount - 1
    var2 = product.amount
    
    if (var1 == 50 and var2 == 49):
        messages.success(request, 'Low on product, order sent to supplier! Refresh page to clear message.')
    product.save()
    return HttpResponseRedirect(reverse('prodTable'))


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