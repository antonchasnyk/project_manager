from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Footprint(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(max_length=30)
    footprint = models.ForeignKey(Footprint)
    image = models.ImageField(upload_to='components_images', null=False, blank=False)
    detail_name = models.CharField(max_length=30, editable=False)
    comment = models.CharField(max_length=80, editable=False)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('component:{}'.format(self.detail_name), kwargs={'id':self.pk})


class Resistor(Component):
    value = models.PositiveIntegerField(default=0) # TODO validator k, M, G

    class Meta:
        ordering = ['footprint', 'value']

    def save(self, *args, **kwargs):
        if not self.detail_name:
            self.detail_name = 'resistor_detail'
        self.comment = '{} {} {}'.format(self.name, self.footprint, res_obfuscator(self.value))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comment


class Capacitor(Component):
    value = models.PositiveIntegerField(default=0)
    voltage = models.PositiveIntegerField(default=5)

    class Meta:
        ordering = ['footprint', 'value']

    def save(self, *args, **kwargs):
        if not self.detail_name:
            self.detail_name = 'capacitor_detail'
        self.comment = '{} {} x {}V {}'.format(self.name, cap_obfuscator(self.value), self.voltage, self.footprint)
        super().save(*args, **kwargs)


class Transistor(Component):
    type = models.CharField(max_length=20)

    class Meta:
        ordering = ['type', 'footprint']

    def save(self, *args, **kwargs):
        if not self.detail_name:
            self.detail_name = 'transistor_detail'
        if not self.comment:
            self.comment = '{} Case type({})'.format(self.name, self.footprint)
        super().save(*args, **kwargs)