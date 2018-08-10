#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.utils import timezone

from .models import User, Question, Answer, Tag

class MainPageView(TemplateView):
    template_name = 'main.html'

class AskPageView(TemplateView):
    template_name = 'ask.html'

class AnswerPageView(TemplateView):
    template_name = 'answer.html'

class SearchPageView(TemplateView):
    template_name = 'search.html'

class TagPageView(TemplateView):
    template_name = 'tag.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class SignupPageView(TemplateView):
    template_name = 'signup.html'

class UserPageView(TemplateView):
    template_name = 'user.html'