from django.contrib import admin
from .models import *
import copy

# admin.site.register(TypeComponents)
# admin.site.register(CompItems)
admin.site.register(Country)
# admin.site.register(Quantity)
admin.site.register(Part)


# @admin.register(Quantity)
# class QuantityAdmin(admin.ModelAdmin):
#     list_display = ('kol',)

@admin.register(TypeComponents)
class TypeComponentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_type')


@admin.register(Components)
class ComponentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_type', 'part_name',  'serial_number', 'country', 'date_of_arrival')
    list_filter = ('name', 'name_type', 'part_name', 'serial_number', 'date_of_arrival')


@admin.register(CompItems)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('comp', 'items', 'quantity')
    list_filter = ('comp', 'items')


def rename_serial(numb):
    a = numb.split('-')
    b = a[:len(a)-1]
    b.append(str(int(a[-1]) + 1).zfill(len(a[-1])))
    return '-'.join(b)


@admin.register(Comp)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'part', 'get_items')
    list_filter = ('serial_number', 'part')
    actions = ['make_copy']

    def make_copy(self, request, queryset):

        for obj in queryset:
            obj_copy = copy.copy(obj)  # (2) django copy object
            obj_copy.id = None  # (3) set 'id' to None to create new object
            obj_copy.serial_number = rename_serial(obj_copy.serial_number)
            obj_copy.save()  # initial save
            for item in obj.items.all():
                obj_copy.items.add(item)
            obj_copy.save()

        c = TypeComponents.objects.get(name_type='Жесткий диск')
        # print('!!!!!!!!!!')
        # print(c.all_items.all())
        # # print(c.all_items.all())
        # print('!!!!!!!!!!')
    make_copy.short_description = "Создать копию"


# def copy_semester(modeladmin, request, queryset):
#     # sd is an instance of SemesterDetails
#     for sd in queryset:
#         sd_copy = copy.copy(sd)  # (2) django copy object
#         sd_copy.id = None  # (3) set 'id' to None to create new object
#         sd_copy.save()  # initial save
#
#         # (4) copy M2M relationship: instructors
#         for instructor in sd.instructors.all():
#             sd_copy.instructors.add(instructor)
#
#         # (5) copy M2M relationship: requirements_met
#         for req in sd.requirements_met.all():
#             sd_copy.requirements_met.add(req)
#
#         # zero out enrollment numbers.
#         # (6) Use __dict__ to access "regular" attributes (not FK or M2M)
#         for attr_name in ['enrollments_entered', 'undergrads_enrolled', 'grads_enrolled', 'employees_enrolled',
#                           'cross_registered', 'withdrawals']:
#             sd_copy.__dict__.update({attr_name: 0})
#
#     sd_copy.save()  # (7) save the copy to the database for M2M relations
#
#     copy_semester.short_description = "Make a Copy of Semester Details"






# @admin.register(Computer)
# class ComputerAdmin(admin.ModelAdmin):
#    list_display = ('serial_number', 'get_components')
#
# @admin.register(ComputerItems)
# class ComputerAdmin(admin.ModelAdmin):
#    list_display = ('id', 'type_components_quantity')

