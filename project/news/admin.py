from django.contrib import admin
from .models import Category, News


    def nullfy_quantity(modeladmin, request, queryset):
        queryset.update(quantity=0)
    nullfy_quantity.short_description = 'Обнулить новости'
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'on_stock')
    list_filter = ('price', 'quantity', 'name')
    search_fields = ('name', 'category__name')
    actions = [nullfy_quantity]

admin.site.register(Category)
admin.site.register(News, NewsAdmin)