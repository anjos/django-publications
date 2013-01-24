#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Fri 17 Oct 09:36:48 2008 

"""Tags to help coding your templates.
"""

from django import template
register = template.Library()

from publications.models import *

@register.inclusion_tag('publications/embed/last.html')
def last_publications(n, include_header):
  """Puts out a bubble with the latest 'n' publications."""
  return {'objects': Publication.objects.order_by('-date')[:n],
          'include_header': include_header}
