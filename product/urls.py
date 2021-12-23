from django.urls import path
from . import views

app_name='product'

urlpatterns = [
    path('', views.product_list , name='home'),
    path('addproduct/', views.add_product , name='add_product'),
    path('dashboard/', views.dashboard , name='dashboard'),
    # path('profile/', views.profile , name='profile'),
    path('orderhistory/', views.order_history , name='orderhistory'),
    path('manageorder/', views.manage_order , name='manageorder'),
    path('<slug:slug>', views.product_detail , name='product_detail'),
    path('mens/' , views.cat_men , name='mens'),
    path('womens/' , views.cat_women , name='womens'),
    path('kids/' , views.cat_kid , name='kids'),
    path('search/' , views.product_list_search , name='search'),
    path('<slug:slug>/delete/' , views.delpro , name='delete'),
    path('<slug:slug>/update/' , views.update_pro , name='update'),
    # path('ContactUs/' , views.contact , name='contact'),
    path('ContactUs/' , views.email,name='contact'),
    path('about/', views.about, name='about'),
    path('buyinfo/', views.buyinfo, name='buyinfo'),
    path('policy/', views.policy, name='policy'),
    path('cond/', views.cond, name='cond'),
    # path('thanks/', views.thanks,name='thanks'),
]