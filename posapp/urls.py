from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    
    path('add_emp/', views.add_emp, name='add_emp'),
    # path('add_cust/', views.add_customer, name='add_cust'),
    # path('add_product/', views.add_product, name="add_product"),
    
    # path('adminVend/', views.adminVend, name="adminVend"),
    # path('empTrans/', views.empTrans, name="empTrans"),
    # path('custRep/', views.custRep, name="custRep"),
    # path('EmpHome/', views.EmpHome, name='EmpHome'),
    
    
    # path('custTrans/', views.custTrans, name='custTrans'),
    path('empTable/', views.empTable, name="empTable"),
    path('custTable/', views.custTable, name="custTable"),
    # path('productTable/', views.productTable, name="productTable"),
    path('prodTable/', views.prodTable, name='prodTable'),
    path('transactionTable/', views.transactionTable, name='transactionTable'),
    
    
    # # Deleting Things
    # path('custTable/delete/<int:id>/', views.delete, name='delete'),
    # path('deleteEmp/<int:id>/', views.deleteEmp, name='deleteEmp'),
    # path('deleteProduct/<int:id>/', views.deleteProduct, name='deleteProduct'),
    
    # path('cart/', views.cart, name='cart'),
    # path('vreg/', views.vreg, name='vreg'),
    path('shop/', views.shop, name='shop'),
    

    # path('pie_chart/',views.pie_chart, name="pie_chart"),
]
