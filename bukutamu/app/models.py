from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin(User):
  class Meta:
    proxy = True
    app_label = 'auth'
    verbose_name = 'Admin'

class Tamu(models.Model):
  nama = models.CharField(max_length= 255, verbose_name= "Nama")
  namaInstansi = models.CharField(max_length= 255, verbose_name= "Nama Instansi")
  jaminan = models.CharField(max_length= 255, verbose_name= "Jaminan")
  keperluan = models.TextField(verbose_name= "Keperluan")
  namaKaryawan = models.CharField(max_length= 255, verbose_name= "Nama Karyawan")
  jumlahTamu = models.IntegerField(default= 1, verbose_name= "Jumlah Tamu")
  foto = models.ImageField(upload_to= 'images', verbose_name= "Foto")
  waktu = models.DateTimeField(auto_now_add= True, verbose_name= "Waktu")

  class Meta: 
    db_table = 'Tamu'
    verbose_name = 'Guest'

  def __str__(self):
    return self.nama

