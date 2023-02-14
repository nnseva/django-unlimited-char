from __future__ import print_function, absolute_import

from django.db import models
from django.utils.translation import gettext_lazy as _

from unlimited_char.fields import CharField


class UnlimitedExample(models.Model):
    """ Import Example """

    name = CharField(
        db_index=True,
        default='',
        verbose_name=_('Name'),
    )

    code = CharField(
        max_length=12,
        db_index=True,
        default='',
        verbose_name=_('Code'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Unlimuted Example')
        verbose_name_plural = _('Unlimited Examples')
