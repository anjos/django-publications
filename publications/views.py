#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Tue 18 Nov 15:52:08 2008 

"""Specialized views for publications.
"""

from django.shortcuts import render_to_response
from django.template import RequestContext, Context, loader
from django.http import HttpResponse

from publications.models import Publication 
from publications.feeds import * 

feeds = { LatestPublications.basename: LatestPublications, 
          LatestFiles.basename   : LatestFiles,
        }


def short_list(request):
  """A personalized listing of publications"""

  data = {}
  for p in Publication.objects.filter(importance__gte=3).order_by('-date'):
    if data.has_key(p.date.year): data[p.date.year].append(p)
    else: data[p.date.year] = [p]

  years = data.keys()
  years.sort(reverse=True)

  data = [(y, data[y]) for y in years]

  return render_to_response('publications/short_list.html',
                            {'objects_by_year': data, 
                             'feeds': feeds.values(),
                            },
                            context_instance=RequestContext(request))

def publications_by_year(request):
  """A personalized listing of publications"""

  data = {}
  for p in Publication.objects.order_by('-date'):
    if data.has_key(p.date.year): data[p.date.year].append(p)
    else: data[p.date.year] = [p]

  years = data.keys()
  years.sort(reverse=True)

  data = [(y, data[y]) for y in years]

  return render_to_response('publications/by_year.html',
                            {'objects_by_year': data, 
                             'feeds': feeds.values(),
                            },
                            context_instance=RequestContext(request))

def simple_list(request):
  """A simple listing of publications"""

  data = {}
  for p in Publication.objects.order_by('-date'):
    if data.has_key(p.date.year): data[p.date.year].append(p)
    else: data[p.date.year] = [p]

  years = data.keys()
  years.sort(reverse=True)

  data = [(y, data[y]) for y in years]

  return render_to_response('publications/simple_list.html',
                            {'objects_by_year': data, 
                            },
                            context_instance=RequestContext(request))

def bibtex_list(request):
  """A simple bibtex listing from my publications"""

  response = HttpResponse(mimetype='application/x-bibtex')
  response['Content-Disposition'] = 'attachment; filename="andreanjos.bib"'

  data = {}
  for p in Publication.objects.order_by('-date'):
    if data.has_key(p.date.year): data[p.date.year].append(p)
    else: data[p.date.year] = [p]

  years = data.keys()
  years.sort(reverse=True)

  data = [(y, data[y]) for y in years]

  t = loader.get_template('publications/list.bib')
  c = Context({
    'objects_by_year': data,
    'site': request.build_absolute_uri('/')[:-1]
    })
  response.write(t.render(c))
  return response
