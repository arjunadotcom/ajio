# Generated by Django 4.1.4 on 2023-02-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_orders_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]