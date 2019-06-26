from django.contrib import admin
from .models import TypeComponents, Country,  Components, Part, Computer

admin.site.register(TypeComponents)
admin.site.register(Country)
# admin.site.register(Computer)
admin.site.register(Part)
@admin.register(Components)
class ComponentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_type', 'part_name', 'serial_number', 'country', 'date_of_arrival')
    list_filter = ('name', 'name_type', 'part_name', 'serial_number', 'date_of_arrival')
@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
   list_display = ('serial_number', 'get_components', 'part_name')

