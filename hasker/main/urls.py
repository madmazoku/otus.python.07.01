#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MainPageView.as_view(), name='main'),
    url(r'^ask$', views.AskPageView.as_view(), name='ask'),
    url(r'^answer$', views.AnswerPageView.as_view(), name='answer'),
    url(r'^search$', views.SearchPageView.as_view(), name='search'),
    url(r'^tag$', views.TagPageView.as_view(), name='tag'),
    url(r'^login$', views.LoginPageView.as_view(), name='login'),
    url(r'^signup$', views.SignupPageView.as_view(), name='signup'),
    url(r'^user$', views.UserPageView.as_view(), name='user'),
]