# Generated by Django 4.2.6 on 2023-10-22 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pooltables', '0020_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='avatar.jpg', upload_to='images')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='pooltables.customers')),
            ],
        ),
    ]
