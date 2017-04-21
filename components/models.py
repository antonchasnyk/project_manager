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
    detail_name = models.CharField(max_length=30, editable=False)
    comment = models.CharField(max_length=80, editable=False)

    def __str__(self):
        return self.comment


def res_obfuscator(value):
    def get_unit(value):
        return {
                      value < 10**3 : ('', 1),
             10**3 <= value < 10**6 : ('k', 10**3),
             10**6 <= value < 10**9 : ('M', 10**6),
             10**9 <= value < 10**12: ('G', 10**9),
            10**12 <= value         : ('T', 10**12)
        }[True]
    multiplier = get_unit(value)
    return '{: 3,.2f} {}Ohm'.format(value/multiplier[1],multiplier[0])


class Resistor(Component):
    value = models.PositiveIntegerField(default=0) # TODO validator k, M, G

    class Meta:
        ordering = ['footprint', 'value']

    def save(self, *args, **kwargs):
        if not self.detail_name:
            self.detail_name = 'resistor_detail'
        self.comment = '{} {} {}'.format(self.name, self.footprint, res_obfuscator(self.value))
        super(Resistor, self).save(*args, **kwargs)

    def __str__(self):
        return self.comment


def cap_obfuscator(value):
    def get_unit(value):
        return {
                      value < 10**3 : ('p', 1),
             10**3 <= value < 10**6 : ('n', 10**3),
             10**6 <= value < 10**9 : ('u', 10**6),
             10**9 <= value < 10**12: ('', 10**9),
            10**12 <= value         : ('k', 10**12)
        }[True]
    multiplier = get_unit(value)
    return '{: 3,.2f} {}F'.format(value/multiplier[1],multiplier[0])


class Capacitor(Component):
    value = models.PositiveIntegerField(default=0)
    voltage = models.PositiveIntegerField(default=5)

    class Meta:
        ordering = ['footprint', 'value']

    def save(self, *args, **kwargs):
        if not self.detail_name:
            self.detail_name = 'capacitor_detail'
        self.comment = '{} {} x {}V {}'.format(self.name, cap_obfuscator(self.value), self.voltage, self.footprint)
        super(Capacitor, self).save(*args, **kwargs)


class Transistor(Component):
    type = models.CharField(max_length=20)

    class Meta:
        ordering = ['type', 'footprint']

    def save(self, *args, **kwargs):
        if not self.detail_name:
            self.detail_name = 'transistor_detail'
        if not self.comment:
            self.comment = '{} Case type({})'.format(self.name, self.footprint)
        super(Transistor, self).save(*args, **kwargs)