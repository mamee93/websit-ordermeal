# Generated by Django 2.2 on 2019-05-20 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_list', '0002_order_price_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price_order',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='meal_list.Meal', verbose_name='سعر الوجبة'),
        ),
    ]