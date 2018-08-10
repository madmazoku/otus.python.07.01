#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

import os

# Create your models here.

def upload_avatar_path(instance, filename):
    suffix_pos = filename.rfind('.')
    suffix_pos = suffix_pos + 1 if suffix_pos != -1 else 0
    p = os.path.join('avatar', '{:d}.{:s}'.format(instance.id, filename[suffix_pos:]))
    return p

class User(models.Model):
    email = models.EmailField(null=True, blank=True)
    login = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to=upload_avatar_path)
    create_date = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.login

class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('User', related_name='question_author')
    create_date = models.DateField(auto_now_add=True, editable=False)
    tag = models.ManyToManyField('Tag', related_name='tag', blank=True)
    like = models.ManyToManyField('User', related_name='question_like', blank=True)
    answer = models.ForeignKey('Answer', related_name='answer', null=True, blank=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey('Question', related_name='question')
    content = models.TextField()
    author = models.ForeignKey('User', related_name='answer_author')
    create_date = models.DateField(auto_now_add=True, editable=False)
    like = models.ManyToManyField('User', related_name='answer_like', blank=True)

    def __str__(self):
        return self.content[:80]

class Tag(models.Model):
    content = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.content
