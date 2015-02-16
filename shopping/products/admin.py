from django.contrib import admin
from models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display = ('__unicode__','slug')
	list_display_links=('__unicode__','slug')
	
admin.site.register(Product, ProductAdmin)