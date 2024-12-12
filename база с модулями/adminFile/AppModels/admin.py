from django.contrib import admin
from AppModels.models import IceCreamShop, IceCream, Parent, Child, News
# Register your models here.

# super user rer 123

class IceCreamShopAdmin(admin.ModelAdmin):
    list_display = ('id_shop', 'name', 'location', 'popolarity', 'opening_hours', 'contact_info', 'owner' ) 
    search_fields = ('id_shop',)  
    list_filter = ('location', 'id_shop', 'name')
    ordering = ('id_shop', 'name')

class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'ShopId')
    search_fields = ('name',)

class ParentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'parent')
    list_filter = ('parent',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'price', 'published')
    list_filter = ('id', )


admin.site.register(IceCreamShop, IceCreamShopAdmin)
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(News, NewsAdmin)
