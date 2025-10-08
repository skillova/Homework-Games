from django.contrib import admin
from .models import Game

@admin.register(Game)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'description', 'image', 'link')