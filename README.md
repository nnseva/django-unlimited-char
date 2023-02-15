[![Tests with Django v2-v3](https://github.com/nnseva/django-unlimited-char/actions/workflows/test-django2-3.yml/badge.svg)](https://github.com/nnseva/django-unlimited-char/actions/workflows/test-django2-3.yml)

[![Tests with Django v3-v4](https://github.com/nnseva/django-unlimited-char/actions/workflows/test-django3-4.yml/badge.svg)](https://github.com/nnseva/django-unlimited-char/actions/workflows/test-django3-4.yml)

# Django-Unlimited-Char

The tiny library introducing CharField with unlimited maximum length.

## Installation

*Stable version* from the PyPi package repository
```bash
pip install django-unlimited-char
```

*Last development version* from the GitHub source version control system
```bash
pip install git+git://github.com/nnseva/django-unlimited-char.git
```

## Compatibility restrictions

**NOTICE** Not all database backends support this feature. At the moment this is
PostgreSQL and SQLite. The Oracle backend supports such a field (not checked yet) partially only.

## Using

```python
from django.db import models

from unlimited_char.fields import CharField

class MyModel(models.Model):
    name = CharField()
    ...
```

You can use this field anywhere the usual CharField is used.

You can assign a max_length attribute as for the original CharField, but this attribute will
restrict the input only (form `clean()` etc). The direct `save()` will not restrict the field length.
