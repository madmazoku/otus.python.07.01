#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.test import TestCase, SimpleTestCase
from django.core.urlresolvers  import reverse
from .models import Post

# Create your tests here.
class HelloTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

class ModelTests(TestCase):
    def setUp(self):
        Post.objects.create(text="just a test")

    def test_post_content(self):
        post = Post.objects.get(id=1)
        got = '{!s}'.format(post.text)
        self.assertEqual(got, "just a test")

class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')