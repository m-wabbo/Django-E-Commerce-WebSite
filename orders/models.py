from django.db import models 
from product.models import Product
from acounts.models import Profile

class Order(models.Model):
    # customer = models.ForeignKey(Profile, null=True, on_delete= models.SET_NULL)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=16)
    # postal_code = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
	# coupon 		= models.ForeignKey(Coupons,related_name='orders',on_delete=models.CASCADE ,null=True,blank=True)
	# discount 	= models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
	
    class Meta:
        ordering = ('-created',)
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
	product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	class Meta:
		verbose_name = "OrderItem"
		verbose_name_plural = "OrderItems"


	def __str__(self):
		return '{}'.format(self.id)


	def get_cost(self):
		return self.price * self.quantity