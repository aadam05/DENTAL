from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'fullName', 'phoneNumber', 'email', 'disease')
    list_display_links = ('fullName',)
    search_fields = ('fullName',)
    list_filter = ('disease',)


class AboutAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'slug')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class ContactAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'slug')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class ServicesAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'slug')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Services, ServicesAdmin)




