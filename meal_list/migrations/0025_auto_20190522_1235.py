# Generated by Django 2.2 on 2019-05-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_list', '0024_auto_20190522_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
