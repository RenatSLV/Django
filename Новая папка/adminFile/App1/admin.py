from django.contrib import admin
from .models import *

# Register your models here.
class BdAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'about_customers', 'published')
    list_display_links = ('name', 'about_customers')
    search_fields = ('name', 'surname')

admin.site.register(Customers, BdAdmin)