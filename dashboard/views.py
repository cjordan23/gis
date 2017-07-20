# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from highcharts.views import HighChartsBarView



# Create your views here.
def dashboard(request):
    return render(request,'dashboard/base.html')
