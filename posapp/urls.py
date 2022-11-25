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
    path('add_vendors/', views.add_vendors, name="add_vendors"),
    
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
    path('vendTable/', views.vendTable, name='vendTable'),
    
    # # Deleting Things
    path('deleteCust/<int:id>/', views.deleteCust, name='delete'),
    path('deleteEmp/<int:id>/', views.deleteEmp, name='deleteEmp'),
    path('deleteProduct/<int:id>/', views.deleteProduct, name='deleteProduct'),
    path('deleteCategory/<int:id>/', views.deleteCategory, name='deleteCategory'),
    path('deleteVendor/<int:id>/', views.deleteVendor, name='deleteVendor'),

    ## Updating Things
    path('updateEmp/<int:id>/', views.updateEmp, name='updateEmp'),
    path('empSubmit/<int:id>', views.empSubmit, name='empSubmit'),
    
    path('updateCust/<int:id>/', views.updateCust, name='updateCust'),
    path('custSubmit/<int:id>', views.custSubmit, name='custSubmit'),
    
    path('updateProd/<int:id>/', views.updateProd, name='updateProd'),
    path('prodSubmit/<int:id>', views.prodSubmit, name='prodSubmit'),
    
    path('updateVendor/<int:id>/', views.updateVendor, name='updateVendor'),
    path('vendSubmit/<int:id>', views.vendSubmit, name='vendSubmit'),
    
    path('updateCategory/<int:id>', views.updateCategory, name='updateCategory'),
    path('categorySubmit/<int:id>', views.categorySubmit, name='categorySubmit'),
    
    # path('vreg/', views.vreg, name='vreg'),
    path('buyProd/<int:id>', views.buyProd, name='buyProd'),

    path('shop/', views.shop, name='shop'),
    

    # path('pie_chart/',views.pie_chart, name="pie_chart"),

    path('one/', views.one, name='one'),
    path('two/', views.two, name='two'),
    path('three/', views.three, name='three'),


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
