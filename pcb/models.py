from django.db import models
from components.models import Component
from django.utils.translation import ugettext as _
import os

# Create your models here.


class Pcb(models.Model):
    """ 
        Represent PCB with link to documentation and BOMs
        Indexing: Name, Cipher, Cipher & Revision 
    """
    name = models.CharField(_('Наименовение'), db_index=True, max_length=30)
    cipher = models.CharField(_('Шифр'), db_index=True, max_length=15)
    revision = models.CharField(_('Ревизия'), max_length=1)
    pcb = models.FileField(_('Монтажный чертеж'), upload_to='pcb')
    orderlist  = models.FileField(_('Лист заказ'), upload_to='order_list')
    orderfiles = models.FileField(_('Архив для заказа'), upload_to='order_files')
    project = models.CharField(_('Ссылка на проект'), max_length=300)

    class Meta:
        unique_together = (('cipher', 'revision'),)
        index_together = (('cipher', 'revision'),)
        ordering = 'cipher', 'revision'
        verbose_name = _('Печатная плата')
        verbose_name_plural = _('Печатные платы')

    def __str__(self):
        return '({} REV. {}) {}'.format(self.cipher, self.revision, self.name)

    # define clean files name

    def clean_pcb(self):
        return os.path.basename(self.pcb.name)

    def clean_orderlist(self):
        return os.path.basename(self.orderlist.name)

    def clean_orderfiles(self):
        return os.path.basename(self.orderfiles.name)


class Schematic(models.Model):
    """
        Represent schematic sheets of pcb
        One PCB can have one or several sheets of schematic
    """
    sheet = models.CharField(_('Лист'), max_length=20)
    sch = models.FileField(_('Файл схемы'), upload_to='schematic')
    pcb = models.ForeignKey(Pcb, verbose_name=_('Печатная плата'))

    class Meta:
        verbose_name = _('Схема принципиальная электрическая')
        verbose_name_plural = _('Схемы принципиальные электрические')

    def __str__(self):
        return 'Sheet {}'.format(self.sheet)

    # define clean files name

    def clean_sch(self):
        return os.path.basename(self.sch.name)


class BomComponent(models.Model):
    """
        ManyToMany pass through table with additional field "annotation" for each element
        wich represent annotation element in schematic
    """
    component = models.ForeignKey(Component, verbose_name=_('Элемент'))
    bom = models.ForeignKey('Bom', verbose_name=_('Перечень элементов'))
    annotation = models.CharField(_('Позиционное обозначение'), max_length=10)

    class Meta:
        unique_together = (('component', 'bom', 'annotation'),)
        verbose_name = _('Компонент')
        verbose_name_plural = _('Компоненты')

    def __str__(self):
        return str(self.component)


class Bom(models.Model):
    """
        Represent Bill of material of PCB. 
        Linked to the components app as ManyToMany
    """
    pcb = models.ForeignKey(Pcb, verbose_name=_('Печатная плата'))
    active = models.BooleanField(_('Рабочая'), default=True)
    components = models.ManyToManyField(Component, through=BomComponent, verbose_name=_('Компоненты'))
    description = models.CharField(_('Описание'), max_length=60)

    class Meta:
        ordering = 'pcb',
        verbose_name = _('Перечень элементов')
        verbose_name_plural = _('Перечни элементов')

    def __str__(self):
        return 'BOM {} {}'.format(self.pcb, self.description)


