from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=60 , null=True,blank=True)
    COUN_CHOIESES = (
        ('egypt', 'مصر'),
        ('doubai','دبى'),
        ('soudia','السعودية')
    )
    phone = models.CharField(max_length=16, blank=True, null=True)
    country = models.CharField(max_length=10, choices=COUN_CHOIESES, default='egypt')
    bdate = models.DateField(blank=True,null=True)
    pic = models.ImageField(upload_to='picusers/admins/',default='picusers/no.png')

    
    def __str__(self):
        return self.user.username