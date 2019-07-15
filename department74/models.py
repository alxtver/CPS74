from django.conf import settings
from django.db import models

from django.db.models import ForeignKey
from django.utils import timezone


class TypeComponents(models.Model):
    id = models.AutoField(primary_key=True)
    name_type = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name_type


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.country


class Part(models.Model):
    id = models.AutoField(primary_key=True)
    part_name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.part_name


class CompItems(models.Model):
    comp = models.ForeignKey('Comp', verbose_name='Серийный номер машины', on_delete=models.CASCADE)
    items = models.ForeignKey('TypeComponents', verbose_name='Тип', on_delete=models.CASCADE)
    quantity = models.ForeignKey('Quantity', default=1,  on_delete=models.CASCADE)

    # def get_quantity(self):
    #     return [i for i in self.quantity.all()]

    def __str__(self):
        """String for representing the Model object."""
        return self.comp.serial_number + ' ' + str(self.quantity)


class Quantity (models.Model):
    kol = models.IntegerField(default=1)

    def __int__(self):
        return self.kol

    def __str__(self):
        return str(self.kol)


class Comp(models.Model):
    serial_number = models.CharField(max_length=200, default=None)
    items = models.ManyToManyField(TypeComponents, through=CompItems, related_name='all_items')
    part = models.ForeignKey(Part, null=True, on_delete=models.CASCADE)

    def get_items(self):
        return [item for item in self.items.all()]

    def __str__(self):
        """String for representing the Model object."""
        return self.serial_number


class Components(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=255, unique=True)
    name_type = models.ForeignKey(TypeComponents, null=False, on_delete=models.CASCADE,
                                  help_text='Тип комплектующих')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True,
                                help_text='Страна производства')
    date_of_arrival = models.DateTimeField(auto_now_add=True)
    part_name = models.ForeignKey(Part, blank=True, null=True, on_delete=models.CASCADE)
    # computer = models.ForeignKey(Computer, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, Серийный номер - {1}'.format(self.name, self.serial_number)
