from django.contrib import admin
from listings import models
# Register your models here.

class ListingImage(admin.TabularInline):
    model=models.Image

class VehicleAdmin(admin.ModelAdmin):
    inlines = [ListingImage,]

admin.site.register(models.Make)
admin.site.register(models.Model)
admin.site.register(models.VehicleSize)
admin.site.register(models.Vehicle, VehicleAdmin)