#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Seg 14 Set 2009 14:42:06 CEST 

"""Installation instructions for publications
"""

from setuptools import setup, find_packages

setup(

    name = "django-publications",
    version = "0.1", 
    packages = find_packages(),

    # we also need all translation files and templates
    package_data = {
      'publications': [
        'templates/publications/*.html',
        'templates/publications/feeds/*.html',
        'templates/publications/embed/*.html',
        'media/css/*.css',
        'media/img/*',
        'locale/*/LC_MESSAGES/django.po',
        'locale/*/LC_MESSAGES/django.mo',
        ],
      },

    zip_safe=False,

    install_requires = [
      'django',
      'docutils',
      'textile',
      ],

    # metadata for upload to PyPI
    author = "Andre Anjos",
    author_email = "andre.dos.anjos@gmail.com",
    description = "Provides a framework to manage publications and documents",
    license = "PSF",
    keywords = "django publications documents",
    url = "",   # project home page, if any
    
)

