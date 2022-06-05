
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
        response = self.client.get('/projects/<int:pk>/')
        self.assertEqual(response.status_code, 200)

    def test_project_detail_page_status_code(self):
        response = self.client.get('/projects/1/')
        self.assertEqual(response.status_code, 200)

    def test_project_create_page_status_code(self):
        response = self.client.get('/projects/new/', args='1')
        self.assertEqual(response.status_code, 302)


class SimpleTests(SimpleTestCase):

    def test_project_create_page_status_code(self):
        response = self.client.get('/projects/new/', args='1')
        self.assertEqual(response.status_code, 302)


# ####################  TEMPLATE CHECKS #####################
#     def test_dashboard_page_returns_correct_template(self):
#         response = self.client.get("/")
#         self.assertTemplateUsed(response, "dashboard.html")
#         self.assertTemplateUsed(response, "icon-nav.html")

#     def test_project_list_returns_correct_template(self):
#         response = self.client.get("/list/")
#         self.assertTemplateUsed(response, "projects/list.html")
#         self.assertTemplateUsed(response, "icon-nav.html")
    
#     def test_project_detail_returns_correct_template(self):
#         response = self.client.get("/<int:pk>/")
#         self.assertTemplateUsed(response, "projects/detail.html")
#         self.assertTemplateUsed(response, "icon-nav.html")
        
#     def test_project_create_returns_correct_template(self):
#         response = self.client.get("/new/")
#         self.assertTemplateUsed(response, "projects/new.html")
#         self.assertTemplateUsed(response, "icon-nav.html")


# # ##################### CONTENT CHECKS ###################
#     def test_dashboard_page_returns_correct_content(self):
#         response = self.client.get("/")
#         self.assertContains("Welcome to your Dash")

#     def test_project_list_page_returns_correct_content(self):
#         response = self.client.get("/list/")
#         self.assertContains("Test Project")
    
#     def test_project_detail_page_returns_correct_content(self):
#         response = self.client.get("/<int:pk>/")
#         self.assertContains({{project.title}})
    
#     def test_create_project_page_returns_correct_content(self):
#         response = self.client.get("/")
#         self.assertContains("New Project")

# # #################### REVERSE LOOKUPS ####################
#     def test_dashboard_page_reverse_lookup(self):
#         response = self.client.get(reverse("dashboard"))
#         self.assertEqual(response.status_code, 200)

#     def test_project_list_page_reverse_lookup(self):
#         response = self.client.get(reverse("project_list"))
#         self.assertEqual(response.status_code, 200)

#     def test_project_detail_page_reverse_lookup(self):
#         response = self.client.get(reverse("project_detail"))
#         self.assertEqual(response.status_code, 200)
    
#     def test_create_project_page_reverse_lookup(self):
#         response = self.client.get(reverse("project_new"))
#         self.assertEqual(response.status_code, 200)