# Generated by Django 3.1.7 on 2021-04-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pooltables', '0005_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
