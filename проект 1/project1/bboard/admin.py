from django.contrib import admin
from .models import *

class BdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'published','rubric')
    list_display_links = ('title', 'price')
    search_fields = ('title', 'price')

class Bdcomment(admin.ModelAdmin):
    list_display = ('id', 'comment', 'author')
    list_display_links = ('id', 'comment', 'author')


admin.site.register(Rubric)
admin.site.register(Bb, BdAdmin)
admin.site.register(Spare)
admin.site.register(Car)
admin.site.register(Crypto)
admin.site.register(Comment, Bdcomment)


