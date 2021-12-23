# Generated by Django 3.0.3 on 2020-02-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(max_length=50)),
                ('PRDDescription', models.CharField(max_length=200)),
                ('PRDUnitPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PRDPrand', models.CharField(max_length=50)),
                ('PRDQuantity_Available', models.IntegerField(max_length=50)),
            ],
        ),
    ]
