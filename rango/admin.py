from django.contrib import admin
from rango.models import Category, Page

# Register your models here.

admin.site.register(Category)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
    def __str__(self):
        return self.name

admin.site.register(Page, PageAdmin)