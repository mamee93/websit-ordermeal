# Generated by Django 2.2 on 2019-05-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_list', '0030_auto_20190522_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
