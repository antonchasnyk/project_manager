from django.db import models

# Create your models here.

class Footprint(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(max_length=30)
    footprint = models.ForeignKey(Footprint)
    image = models.ImageField(upload_to='components_images', null=True, blank=True)

    def __str__(self):
        return self.name


class Resistor(Component):
    value = models.PositiveIntegerField(default=0)


class Capacitor(Component):
    value = models.PositiveIntegerField(default=0)


class Transistor(Component):
    type = models.CharField(max_length=20)