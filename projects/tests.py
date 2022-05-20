
from ast import arg
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class DataTests(TestCase):

##################### PAGE STATUS CODES ####################
    def test_dashboard_page_status_code(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)

    def test_project_list_page_status_code(self):
        response = self.client.get('/projects/list/')
        self.assertEqual(response.status_code, 200)

    def test_project_detail_page_status_code(self):
        response = self.client.get('/projects/1/')
        self.assertEqual(response.status_code, 200)


class SimpleTests(SimpleTestCase):

    def test_project_create_page_status_code(self):
        response = self.client.get('/projects/new/', args='1')
        self.assertEqual(response.status_code, 302)
