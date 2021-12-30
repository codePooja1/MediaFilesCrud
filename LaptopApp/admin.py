from django.contrib import admin
from .models import Laptop


class LaptopAdmin(admin.ModelAdmin):
    list_display = ['company', 'model_name', 'ram', 'rom', 'processor', 'price', 'weight', 'picture', 'document']


admin.site.register(Laptop, LaptopAdmin)

