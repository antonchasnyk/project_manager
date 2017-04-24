from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ComponentsConfig(AppConfig):
    name = 'components'
    verbose_name = _('Компоненты печатных плат')
