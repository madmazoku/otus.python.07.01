#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    text = models.TextField()

    @property
    def now(self):
        return timezone.now()

    def __str__(self):
        return self.text[:50]