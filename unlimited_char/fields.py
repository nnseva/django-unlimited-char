"""Field definitions"""
from django.db import models, connection
from django.utils.translation import ugettext_lazy as _
from django.core import validators


class CharField(models.Field):
    description = _("String with unlimited max_length=None available")

    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)
        if self.max_length is not None:
            self.validators.append(validators.MaxLengthValidator(self.max_length))

    def cast_db_type(self, connection):
        return connection.ops.cast_char_field_without_max_length

    def db_type(self, connection):
        return connection.ops.cast_char_field_without_max_length

    def get_internal_type(self):
        return "UnlimitedCharField"

    def to_python(self, value):
        if isinstance(value, str) or value is None:
            return value
        return str(value)

    def get_prep_value(self, value):
        value = super(CharField, self).get_prep_value(value)
        return self.to_python(value)

    def formfield(self, **kwargs):
        defaults = {'max_length': self.max_length}
        # TODO: Handle multiple backends with different feature flags.
        if self.null and not connection.features.interprets_empty_strings_as_nulls:
            defaults['empty_value'] = None
        defaults.update(kwargs)
        return super(CharField, self).formfield(**defaults)
