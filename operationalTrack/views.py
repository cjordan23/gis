# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse



# Create your views here.
def operationalTrack(request):
    return render(request,'operationalTrack/operationalTrack.html')
