from django.contrib import admin
from.models import Grupe
# Register your models here.

@admin.register(Grupe)
class GrupesAdmin(admin.ModelAdmin):
    list_display=["name","adress","num_phone","birth_day","nation"]
    list_display=["name","nation"]
