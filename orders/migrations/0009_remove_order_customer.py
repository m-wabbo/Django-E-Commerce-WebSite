# Generated by Django 3.0.3 on 2020-05-17 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200517_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]
