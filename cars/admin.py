from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'make', 'model', 'rates_number']
    list_filter = ('make',)
