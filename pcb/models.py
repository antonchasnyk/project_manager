from django.db import models
from components.models import Component
from django.core.exceptions import ValidationError
import os

# Create your models here.


def file_pdf(value):    # TODO Validators
    if False:
        raise ValidationError('Only *.pdf are support')
    return value


def file_doc(value):
    if False:
        raise ValidationError('Only *.doc are support')
    return value


def file_zip(value):
    if False:
        raise ValidationError('Only *.zip are support')
    return value


class Pcb(models.Model):
    name = models.CharField(max_length=30)
    cipher = models.CharField(max_length=15)
    revision = models.CharField(max_length=1)
    pcb = models.FileField(upload_to='pcb', validators=[file_pdf])
    orderlist  = models.FileField(upload_to='order_list', validators=[file_doc])
    orderfiles = models.FileField(upload_to='order_files', validators=[file_zip])
    project = models.CharField(max_length=300)

    class Meta:
        unique_together = (('cipher', 'revision'),)
        ordering = 'cipher', 'revision'
        verbose_name = 'PCB'
        verbose_name_plural = 'PCBs'

    def __str__(self):
        return '({} REV. {}) {}'.format(self.cipher, self.revision, self.name)

    def filename(self): # TODO clear filename
        print(os.path.basename(self.orderlist.name))
        return os.path.basename(self.orderlist.name)


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


class Schematic(models.Model):
    sheet = models.CharField(max_length=5)
    sch = models.FileField(upload_to='schematic', validators=[file_pdf])
    pcb = models.ForeignKey(Pcb)

    def __str__(self):
        return 'Sheet {}'.format(self.sheet)