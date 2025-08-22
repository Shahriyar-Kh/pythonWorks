from django.contrib import admin
from .models import *
# Register your models here.
class RecipeM(admin.ModelAdmin):
    list_display=("Recipe_Name",)

admin.site.register(Recipe_tb,RecipeM)

