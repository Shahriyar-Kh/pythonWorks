from django.contrib import admin
from .models import Emplyee
# Register your models here.

class empAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname","phone",)

admin.site.register(Emplyee,empAdmin)
