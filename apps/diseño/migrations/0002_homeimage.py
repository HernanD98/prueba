# Generated by Django 4.2.6 on 2023-11-09 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseño', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=20, unique=True)),
                ('slug', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(max_length=250, unique=True)),
                ('images', models.ImageField(upload_to='home/presentation')),
            ],
        ),
    ]
