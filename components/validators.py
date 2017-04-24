from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re
from decimal import Decimal


def res_validator(in_res):
    unit_to_multiplier = {
        'O': 1,
        'R': 1,
        'K': 10 ** 3,
        'M': 10 ** 6,
        'G': 10 ** 9,
    }
    m = re.match(r"^(?P<digits>[0-9,.]+)\s?(?P<unit>\w*)$", str(in_res), re.IGNORECASE)
    if m:
        res = 0
        if m.group('digits'):
            res = Decimal(m.group('digits'))
        if m.group('unit'):
            try:
                un = unit_to_multiplier[m.group('unit').upper()[0]]
            except KeyError:
                raise ValidationError(_('Undefined units'), code='units')
            res *= un
    else:
        raise ValidationError(_('Undefined formats'), code='format')
    return int(res*1000)


def cap_validator(in_cap):
    unit_to_multiplier = {
        'P': 1,
        'N': 10 ** 3,
        'U': 10 ** 6,
        'M': 10 ** 9,
        'F': 10 ** 12,
    }
    m = re.match(r"^(?P<digits>[0-9,.]+)\s?(?P<unit>\w*)$", str(in_cap), re.IGNORECASE)
    if m:
        cap = 0
        if m.group('digits'):
            cap = Decimal(m.group('digits'))
        if m.group('unit'):
            try:
                un = unit_to_multiplier[m.group('unit').upper()[0]]
            except KeyError:
                raise ValidationError(_('Undefined units'), code='units')
            cap *= un
    else:
        raise ValidationError(_('Undefined formats'), code='format')
    return int(cap*1000)