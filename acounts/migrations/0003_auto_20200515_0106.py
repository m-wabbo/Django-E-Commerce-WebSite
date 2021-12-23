# Generated by Django 3.0.3 on 2020-05-14 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0002_auto_20200419_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(choices=[('egypt', 'مصر'), ('doubai', 'دبى'), ('soudia', 'السعودية')], default='egypt', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='emailAdress',
            field=models.EmailField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]