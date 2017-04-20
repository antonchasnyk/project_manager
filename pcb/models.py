from django.db import models
from components.models import Component

# Create your models here.


class Pcb(models.Model):
    name = models.CharField(max_length=30)
    cipher = models.CharField(max_length=15)
    revision = models.CharField(max_length=1)

    class Meta:
        unique_together = (('cipher', 'revision'),)
        ordering = 'cipher', 'revision'
        verbose_name = 'PCB'
        verbose_name_plural = 'PCBs'

    def __str__(self):
        return '({} REV. {}) {}'.format(self.cipher, self.revision, self.name)


class BomComponent(models.Model):
    component = models.ForeignKey(Component, verbose_name='Component')
    bom = models.ForeignKey('Bom', verbose_name='Bill of material')
    annotation = models.CharField('Annotation', max_length=10)

    class Meta:
        unique_together = (('component', 'bom', 'annotation'),)
        verbose_name = 'Component in Bom'
        verbose_name_plural = 'Components in Bom'


class Bom(models.Model):
    pcb = models.ForeignKey(Pcb)
    active = models.BooleanField(default=False)
    components = models.ManyToManyField(Component, through=BomComponent, verbose_name='components')
    description = models.CharField(max_length=60)
    class Meta:
        ordering = 'pcb',
        verbose_name = 'BOM'
        verbose_name_plural = 'BOMs'

    def __str__(self):
        return 'BOM {} {}'.format(self.pcb, self.description)