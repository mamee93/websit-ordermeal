# Generated by Django 2.2 on 2019-05-20 10:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_meal', models.CharField(max_length=100, verbose_name='اسم الوجبة')),
                ('content', models.TextField(verbose_name='وصف الوجبة')),
                ('image', models.ImageField(blank=True, upload_to='meal-img/%Y/%m/%d')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='سعر الوجبة')),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='الاسم')),
                ('email', models.EmailField(max_length=254, verbose_name='البريد الالكتروني')),
                ('location', models.TextField(verbose_name='العنوان')),
                ('Number_of_meal', models.IntegerField(default=1, verbose_name='عدد الوجبة')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='meal_list.Meal')),
            ],
            options={
                'ordering': ['-order_date'],
            },
        ),
    ]
