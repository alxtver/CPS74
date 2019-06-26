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


class Components(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=255)
    name_type = models.ForeignKey(TypeComponents, on_delete=models.SET_NULL, null=True,
                                  help_text='Тип комплектующих')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True,
                                help_text='Страна производства')
    date_of_arrival = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, Серийный номер - {1}'.format(self.name, self.serial_number)


class Part(models.Model):
    id = models.AutoField(primary_key=True)
    part_name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.part_name


class Computer(models.Model):
    id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100)
    components = models.ManyToManyField(Components, null=True)
    part_name = models.ForeignKey(Part, null=True, on_delete=models.CASCADE)

    def get_components(self):
        return "\n".join([p.name for p in self.components.all()])
