from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from .models import	OrderItem ,Order
from .forms	import OrderCreateForm 
from cart.cart import Cart
from django.urls import reverse
from django.shortcuts import render, redirect

# Create your views here. 
@login_required
def	order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'])
            
            cart.clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return	render(request,'orders/order/create.html',{'cart':	cart, 'form': form })
