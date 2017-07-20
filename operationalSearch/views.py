# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def operationalSearch(request):
    return render(request,'operationalSearch/operationalSearch.html')
