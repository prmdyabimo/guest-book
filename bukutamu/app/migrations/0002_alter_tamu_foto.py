# Generated by Django 4.1.1 on 2022-09-12 03:46

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamu',
            name='foto',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/images'), upload_to=''),
        ),
    ]
