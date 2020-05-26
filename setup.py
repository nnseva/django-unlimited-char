#!/usr/bin/python

"""
A setuptools based setup module.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
from unlimited_char import __version__ as version

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-unlimited-char',

    version=version,
    python_requires='>3.4',

    description='Django-Unlimited-Char - the library introducing unlimited character database field for Django',
    long_description=long_description,

    url='https://github.com/nnseva/django-unlimited-char',

    author='Vsevolod Novikov',
    author_email='nnseva@gmail.com',

    zip_safe=False,
    platforms="any",

    license='LGPL',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'Environment :: Web Environment',

        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',

        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='django field unlimited char postgres sqlite3',
    packages=find_packages(exclude=['dev']),
    install_requires=['django>=2.0', 'six'],
)
