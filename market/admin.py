from django.contrib import admin

from market import models


@admin.register(models.Product)
class DishAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


