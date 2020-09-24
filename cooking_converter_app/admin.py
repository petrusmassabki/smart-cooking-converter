from django.contrib import admin
from . import models


class DisplayIngredients(admin.ModelAdmin):
    list_display = ('id', 'ingredient_name', 'bulk_density', 'category')
    list_display_links = ('id', 'ingredient_name')
    search_fields = ('ingredient_name',)
    list_filter = ('category',)
    list_per_page = 50


admin.site.register(models.Ingredient, DisplayIngredients)