# Generated by Django 2.2 on 2019-05-20 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal_list', '0003_auto_20190520_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price_order',
        ),
    ]
