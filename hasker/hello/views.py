#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render


from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


# from django.http import HttpResponse

# def aboutPageView(request):
#     return HttpResponse('About!')