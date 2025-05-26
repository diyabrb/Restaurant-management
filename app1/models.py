from django.db import models

# Create your models here.

class Menu(models.Model):
    f_name = models.CharField(max_length=100)
    f_desc = models.CharField(max_length=255)
    f_type = models.CharField(max_length=100)
    f_price = models.CharField(max_length=100)

    f_image = models.ImageField(upload_to='menu')   
    #def __str__(self):
     #   return self.f_name + ' (' + self.f_type + ')'
class contact(models.Model):
    f_name = models.CharField(max_length=100)
    f_phone = models.CharField(max_length=10)
    f_email = models.EmailField()
    f_desc = models.CharField(max_length=255)

   
