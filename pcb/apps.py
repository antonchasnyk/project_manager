from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class PcbConfig(AppConfig):
    name = 'pcb'
    verbose_name = _('Печатные платы')
