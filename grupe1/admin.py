from django.contrib import admin
from.models import Grupe1
# Register your models here.

@admin.register(Grupe1)
class Grupe1sAdmin(admin.ModelAdmin):
    list_display=["name","adress","num_phone","birth_day","nation"]
    list_display=["name","nation"]

