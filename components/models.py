from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from .obfuscator import res_obfuscator, cap_obfuscator
from .validators import res_validator

# Create your models here.


class Footprint(models.Model):
    name = models.CharField(_('Наименование'), db_index=True, max_length=30)

    class Meta:
        verbose_name = _('Посадочное место')
        verbose_name_plural = _('Посадочные места')

    def __str__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(_('Партномер'), db_index=True, max_length=30)
    footprint = models.ForeignKey(Footprint, db_index=True, verbose_name=_('Посадочное место'))
    image = models.ImageField(_('Фото'), upload_to='components_images', null=False, blank=False)
    detail_name = models.CharField(max_length=30, editable=False)
    comment = models.CharField(max_length=80, editable=False)

    class Meta:
        verbose_name = _('Компонент')
        verbose_name_plural = _('Компоненты')

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('component:{}'.format(self.detail_name), kwargs={'id':self.pk})


class Resistor(Component):
    value = models.BigIntegerField(_('Номинал'), db_index=True, default=0) # Store in mOhm

    class Meta:
        ordering = ['footprint', 'value']
        verbose_name = _('Резистор')
        verbose_name_plural = _('Резисторы')

    def save(self, *args, **kwargs):
        if not self.detail_name:
            self.detail_name = 'resistor_detail'
        self.comment = '{} {} {}'.format(self.name, self.footprint, self.get_value())
        super().save(*args, **kwargs)

    def get_value(self):
        return res_obfuscator(self.value/1000) # mOhm to Ohm and obfuscate

    def __str__(self):
        return self.comment


class Capacitor(Component):
    value = models.BigIntegerField(_('Номинал'), db_index=True,  default=0)
    voltage = models.FloatField(_('Напряжение'), db_index=True, default=5)

    class Meta:
        ordering = ['footprint', 'value']
        index_together = (('value', 'voltage'),)
        verbose_name = _('Конденсатор')
        verbose_name_plural = _('Конденсаторы')

    def save(self, *args, **kwargs):
        if not self.detail_name:
            self.detail_name = 'capacitor_detail'
        self.comment = '{} {} x {}V {}'.format(self.name, self.get_value(), self.voltage, self.footprint)
        super().save(*args, **kwargs)

    def get_value(self):
        return cap_obfuscator(self.value/1000)

    def get_voltage(self):
        return '{} V'.format(self.voltage)


class Transistor(Component):
    type = models.CharField(_('Тип'), db_index=True, max_length=20)

    class Meta:
        ordering = ['type', 'footprint']
        verbose_name = _('Транзистор')
        verbose_name_plural = _('Транзисторы')

    def save(self, *args, **kwargs):
        if not self.detail_name:
            self.detail_name = 'transistor_detail'
        if not self.comment:
            self.comment = '{} Case type({})'.format(self.name, self.footprint)
        super().save(*args, **kwargs)