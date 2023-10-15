from django.contrib import admin
from .models import City, Dwelling, Photo, OccupiedDate, DwellingType

class DwellingAdmin(admin.ModelAdmin):
    list_display = ['title', 'city', 'dwelling_type', 'guests', 'area']
    search_fields = ['title', 'city__name', 'dwelling_type__type_name']

admin.site.register(Dwelling, DwellingAdmin)

class DwellingTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']
    search_fields = ['type_name']

admin.site.register(DwellingType, DwellingTypeAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(City, CityAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['id']

admin.site.register(Photo, PhotoAdmin)

class OccupiedDateAdmin(admin.ModelAdmin):
    list_display = ['check_in', 'check_out']
    search_fields = ['check_in', 'check_out']

admin.site.register(OccupiedDate, OccupiedDateAdmin)