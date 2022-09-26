from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

admin.site.site_title = 'Administration Page'
admin.site.index_title = 'G-Book'
admin.site.site_header = 'G-Book'
admin.site.register(Admin, UserAdmin)



class TamuAdmin(admin.ModelAdmin):
  list_display = ['id', 'nama', 'namaInstansi', 'jaminan', 'keperluan', 'namaKaryawan', 'jumlahTamu', 'foto', 'waktu']

admin.site.register(Tamu, TamuAdmin)