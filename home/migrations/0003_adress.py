# Generated by Django 4.2.6 on 2023-11-06 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_cart_catagory_order_item_cart_items_cart_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('order_confirmed', models.BooleanField(default=False)),
                ('order_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order')),
            ],
        ),
    ]