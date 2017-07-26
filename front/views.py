# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def FrontView(request):
    #return render(request, 'front/index.html', {})
    return HttpResponse("Currently whatever is here.")

# Create your views here.
