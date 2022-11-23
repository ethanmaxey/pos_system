from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    
    path('add_emp/', views.add_emp, name='add_emp'),
    path('add_cust/', views.add_customer, name='add_cust'),
    path('add_product/', views.add_product, name="add_product"),
    path('add_category/', views.add_category, name="add_category"),
<<<<<<< HEAD
=======
    path('add_vendors/', views.add_vendors, name="add_vendors"),
>>>>>>> 8231de863b239fb7f8c537fa75e0135992921ac6
    
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
    path('catTable/', views.catTable, name='catTable'),
<<<<<<< HEAD
=======
    path('vendTable/', views.vendTable, name='vendTable'),
>>>>>>> 8231de863b239fb7f8c537fa75e0135992921ac6
    
    # # Deleting Things
    path('deleteCust/<int:id>/', views.deleteCust, name='delete'),
    path('deleteEmp/<int:id>/', views.deleteEmp, name='deleteEmp'),
    path('deleteProduct/<int:id>/', views.deleteProduct, name='deleteProduct'),
    path('deleteCategory/<int:id>/', views.deleteCategory, name='deleteCategory'),
<<<<<<< HEAD
=======
    path('deleteVendor/<int:id>/', views.deleteVendor, name='deleteVendor'),
>>>>>>> 8231de863b239fb7f8c537fa75e0135992921ac6

    ## Updating Things
    path('updateEmp/<int:id>/', views.updateEmp, name='updateEmp'),
    path('updateEmp/<int:id>/empSubmit/', views.empSubmit, name='empSubmit'),
    path('updateCust/<int:id>/', views.updateCust, name='updateCust'),
    path('updateCust/<int:id>/custSubmit/', views.custSubmit, name='custSubmit'),
    path('updateProd/<int:id>/', views.updateProd, name='updateProd'),
    path('updateProd/<int:id>/prodSubmit/', views.prodSubmit, name='prodSubmit'),
<<<<<<< HEAD
=======
    path('updateVendor/<int:id>/', views.updateVendor, name='updateVendor'),
    path('updateVendor/<int:id>/vendSubmit/', views.vendSubmit, name='vendSubmit'),
>>>>>>> 8231de863b239fb7f8c537fa75e0135992921ac6
    
    # path('vreg/', views.vreg, name='vreg'),
    path('shop/', views.shop, name='shop'),
    

    # path('pie_chart/',views.pie_chart, name="pie_chart"),



    # url for the cart
    #so let us break this down..
    #cart/


    path('cart/', views.cart, name='cart'), #not sure if this one will work well for me
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),


]
