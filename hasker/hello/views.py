#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.utils import timezone

from .models import Post

class HomePageView(ListView):
    template_name = 'home.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'


# from django.http import HttpResponse

# def aboutPageView(request):
#     return HttpResponse('About!')