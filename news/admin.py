from django.contrib import admin

from .models import Column, Article, IMG


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'home_display')

class IMGAdmin(admin.ModelAdmin):
    list_display = ('name', 'img')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'pub_date', 'update_time')
    list_filter = ('column', 'author', 'pub_date')

admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(IMG, IMGAdmin)
