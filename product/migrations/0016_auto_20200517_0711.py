# Generated by Django 3.0.3 on 2020-05-17 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20200516_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(unique=True),
        ),
    ]