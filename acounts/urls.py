from django.urls import path
from . import views
app_name='acounts'

urlpatterns = [
path('register/' , views.register , name='register'),
path('login/' , views.log_in , name='login'),
path('logout/' , views.log_out , name='logout'),
path('edit/',	views.edit,	name='edit'),
path('profile/',	views.profile,	name='prof'),
# path('<int:id>/updateprofile/' , views.update_profile , name='updateprof'),
# path('customer/<str:pk_test>/', views.customer, name="customer"),
]