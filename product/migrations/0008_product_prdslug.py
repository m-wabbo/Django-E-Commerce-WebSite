# Generated by Django 3.0.3 on 2020-03-05 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200227_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
