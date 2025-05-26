
from django.contrib import admin
from .models import Menu,contact
# Register your models here.
class contactadmin(admin.ModelAdmin):
    list_display=('id','f_name','f_phone','f_email','f_desc')

admin.site.register(contact,contactadmin)

admin.site.register(Menu)



