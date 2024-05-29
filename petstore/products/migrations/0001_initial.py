# Generated by Django 5.0.3 on 2024-04-08 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='product name', max_length=70)),
                ('product_description', models.TextField(default='Description')),
                ('product_price', models.PositiveIntegerField(default=0)),
                ('product_brand', models.CharField(default='superpet', max_length=50)),
                ('product_picture', models.ImageField(null=True, upload_to='products/')),
            ],
        ),
    ]