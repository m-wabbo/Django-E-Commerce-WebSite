from django.db import models
#from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    CATYName = models.CharField(max_length=25, unique=True)
    CATYDescription = models.CharField(max_length=200)
    CATYImage = models.ImageField(upload_to='product/category/')

    def __str__(self):
        return self.CATYName

class Product(models.Model):
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    PRDName = models.CharField(max_length=50)
    PRDDescription = models.CharField(max_length=200)
    PRDUnitPrice = models.DecimalField(max_digits=7 , decimal_places=2)
    PRDPrand = models.CharField(max_length=50)
    PRDImage = models.ImageField(upload_to='product/' , blank=True , null=True)
    PRDImage1 = models.ImageField(upload_to='product/' , blank=True , null=True)
    PRDImage2 = models.ImageField(upload_to='product/' , blank=True , null=True)
    PRDQuantity_Available = models.IntegerField()
    PRODUCT_SIZES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('X Large', 'X Large'),
        ('XX Large', 'XX Large'),
        ('XXX Large', 'XXX Large')
    )
    PRDSize = models.CharField(max_length=15, choices=PRODUCT_SIZES, default='Medium')
    PRDColor = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    PRDSlug = models.SlugField(unique=True)
# لظهور اسم المنتج فى اللينك
    def save(self , *args , **kwargs):
        if not self.PRDSlug:
            self.PRDSlug = slugify(self.PRDName)
        super(Product , self).save(*args , **kwargs)

    def __str__(self):
        return self.PRDName

# class ProductImage(models.Model):
#     PRDIProduct = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name=_("product image"))
#     PRDiImage = models.ImageField(upload_to='product/', verbose_name=_("image"))

    # def __str__(self):
    #     return str(self.PRDIProduct)
