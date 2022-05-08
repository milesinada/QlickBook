from django.urls import path
from .views import DashboardPageView, ProjectListView

urlpatterns = [
    path('', DashboardPageView.as_view(), name='dashboard'),
    path('list/', ProjectListView.as_view(), name='project_list'),
]