# Generated by Django 3.0.3 on 2020-02-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_productsize'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDSize',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X Large'), ('XXL', 'XX Large')], default='M', max_length=4),
        ),
    ]
