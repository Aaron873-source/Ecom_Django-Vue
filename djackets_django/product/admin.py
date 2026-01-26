from django.contrib import admin
from .models import category, Product
# Register your models here.

#Need to register the desired models so they can appear in the Admin panel and we can do CRUD operations to them
admin.site.register(category)
admin.site.register(Product)
