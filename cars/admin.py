from django.contrib import admin

from .models import Car, Rate


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'make', 'model', 'rates_number']
    list_filter = ('make',)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ['id', 'car_id', 'rating']
