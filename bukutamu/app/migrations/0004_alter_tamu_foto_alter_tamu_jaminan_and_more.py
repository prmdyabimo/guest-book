# Generated by Django 4.1.1 on 2022-09-12 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_tamu_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamu',
            name='foto',
            field=models.ImageField(upload_to='images', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='jaminan',
            field=models.CharField(max_length=255, verbose_name='Jaminan'),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='jumlahTamu',
            field=models.IntegerField(default=1, verbose_name='Jumlah Tamu'),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='keperluan',
            field=models.TextField(verbose_name='Keperluan'),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='nama',
            field=models.CharField(max_length=255, verbose_name='Nama'),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='namaInstansi',
            field=models.CharField(max_length=255, verbose_name='Nama Instansi'),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='namaKaryawan',
            field=models.CharField(max_length=255, verbose_name='Nama Karyawan'),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='waktu',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Waktu'),
        ),
    ]