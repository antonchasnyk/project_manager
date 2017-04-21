from django.db import models

# Create your models here.

class Footprint(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(max_length=30)
    footprint = models.ForeignKey(Footprint)
    image = models.ImageField(upload_to='components_images', null=False, blank=False)

    def __str__(self):
        return self.name


class Resistor(Component):
    value = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['footprint', 'value']


class Capacitor(Component):
    value = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['footprint', 'value']


class Transistor(Component):
    type = models.CharField(max_length=20)

    class Meta:
        ordering = ['type', 'footprint']