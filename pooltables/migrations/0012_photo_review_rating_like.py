# Generated by Django 4.2.5 on 2023-10-06 22:13

from django.db import migrations, models
import django.db.models.deletion
import pooltables.models.gallery


class Migration(migrations.Migration):

    dependencies = [
        ('pooltables', '0011_productimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=pooltables.models.gallery.get_upload_path)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pooltables.customer')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pooltables.photo')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pooltables.customer')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pooltables.photo')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pooltables.customer')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pooltables.photo')),
            ],
        ),
    ]
