from django import forms 
from .models import Product  #,ProductImage

class AddProduct(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = "__all__"

# class Contact(forms.Form):
#     name = forms.CharField(max_length=40)
#     email = forms.EmailField(max_length=70)
#     message = forms.CharField( max_length=500, widget= forms.Textarea ) 


# class ContactForm(forms.Form):
#     from_email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(widget=forms.Textarea, required=True)

# class ContactForm(forms.Form):

#     from_email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(widget=forms.Textarea)