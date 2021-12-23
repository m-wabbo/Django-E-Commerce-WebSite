from django.core.paginator import Paginator
from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Product,Category   #,ProductImage
from acounts.forms import Profile
from django.db.models import Q
from .forms import AddProduct    # ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm
from orders.models import Order

# Create your views here.


# def email(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['mahmoudhoda2016@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('thanks')
#     return render(request, "ContactUs.html", {'form': form})

# def thanks(request):
#     return HttpResponse('Thank you for your message.')
# ##############################################################################

def email(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('contact form',message,settings.EMAIL_HOST_USER,['mahmoudhoda2016@gmail.com'],fail_silently=False)
    return render(request, "ContactUs.html")

##########################################################################
def product_list(request):
    product_list = Product.objects.all()
    
    search_query = request.GET.get('q')
    if search_query:
        product_list = product_list.filter(
            Q(PRDName__icontains = search_query)
        )
    prolast = Product.objects.last()
    # pricefilter = Product.objects.order_by('-PRDUnitPrice')
# للتغير بين صفحات الموقع
    paginator = Paginator(product_list, 3) # Show 15 contacts per page.
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)

    

    context = {'product_list': product_list, 'prolast': prolast}
    return render(request,'index.html', context)
##########################################################################
def product_list_search(request):
    product_list_search = Product.objects.all()
    
    search_query = request.GET.get('q')
    if search_query:
        product_list_search = product_list_search.filter(
            Q(PRDName__icontains = search_query)
        )

# للتغير بين صفحات الموقع
    paginator = Paginator(product_list_search, 3) # Show 15 contacts per page.
    page_number = request.GET.get('page')
    product_list_search = paginator.get_page(page_number)

    

    context = {'product_list_search': product_list_search}
    return render(request,'homesearch.html', context)
##########################################################################
def product_detail(request , slug):
    # product_detail = Product.objects.get(PRDSlug=slug)
    product_detail	= get_object_or_404(Product, PRDSlug=slug)
    # productImage = ProductImage.objects.filter(PRDIProduct = product_detail)   
    
    cart_product_form =	CartAddProductForm()

    context = {'product_detail' : product_detail , 'cart_product_form' : cart_product_form}
    return render(request , 'ProductDetail.html' , context)
##########################################################################
def cat_men(request):
    # filtering by category
    men_products = Category.objects.get(CATYName = "رجالى")
    product_list_men = Product.objects.all().filter(Category = men_products)

    paginator = Paginator(product_list_men, 3) # Show 15 contacts per page.
    page_number = request.GET.get('page')
    product_list_men = paginator.get_page(page_number)
    
    context = {'product_list_men': product_list_men , 'men_products' : men_products}
    return render(request , 'Mens.html' , context)
##########################################################################
def cat_women(request):
    # filtering by category
    women_products = Category.objects.get(CATYName = "حريمى")
    product_list_women = Product.objects.all().filter(Category = women_products)

    paginator = Paginator(product_list_women, 3) # Show 15 contacts per page.
    page_number = request.GET.get('page')
    product_list_women = paginator.get_page(page_number)
    
    context = {'product_list_women': product_list_women}
    return render(request , 'womens.html' , context)

def cat_kid(request):
    # filtering by category
    kid_products = Category.objects.get(CATYName = "اطفالى")
    product_list_kid = Product.objects.all().filter(Category = kid_products)

    paginator = Paginator(product_list_kid, 3) # Show 15 contacts per page.
    page_number = request.GET.get('page')
    product_list_kid = paginator.get_page(page_number)
    
    context = {'product_list_kid': product_list_kid}
    return render(request , 'kids.html' , context)
# seller #################################################################
@login_required
def add_product(request):
    if request.method == "GET":
        form = AddProduct()
    else:
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    allpro = Product.objects.all()
    total_products = allpro.count()
    

    context={'add_product': form , 'allpro' : allpro ,'total_products':total_products}
    return render(request, 'seller/ProductManagement.html', context)
#########################################################################
@login_required
def dashboard(request):
    orders = Order.objects.all()
    total_orders = orders.count()
    customers = Profile.objects.all()
    total_customer = customers.count
    allpro = Product.objects.all()
    total_products = allpro.count()
    last_order = Product.objects.last()
    context = {'total_orders':total_orders,'total_customer':total_customer,'total_products':total_products,'last_order':last_order}
    return render(request, 'seller/dash.html', context)
##########################################################################
@login_required
def order_history(request):
    allorders = Order.objects.all()
    context={'allorders':allorders}
    return render(request, 'seller/order_history.html', context)
##########################################################################
@login_required
def manage_order(request):
    return render(request, 'seller/manageorder.html')
##########################################################################
@login_required
def delpro(request, slug):
    deldel = Product.objects.get(PRDSlug=slug)
    if request.method == "POST":
        deldel.delete()
        return HttpResponseRedirect(reverse("products:add_product"))
    return render(request, "seller/deletepro.html",)
##########################################################################
@login_required
def update_pro(request, slug):
    udatepro = Product.objects.get(PRDSlug=slug)
    # form = AddProduct(request.POST or None, instance = udatepro)
    form = AddProduct(request.POST or None, request.FILES or None,  instance=udatepro)
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect(reverse("products:add_product"))
  
    context={'update_pro' : form}
    return render(request, "seller/update_pro.html", context)
##########################################################################
def about(request):
    return render(request, "about.html")

def buyinfo(request):
    return render(request, "buyinfo.html")

def policy(request):
    return render(request, "policy.html")

def cond(request):
    return render(request, "cond.html")
