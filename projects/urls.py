from django.urls import path
from .views import DashboardPageView, ProjectListView, ProjectDetailView, ProjectCreateView

urlpatterns = [
    path('', DashboardPageView.as_view(), name='dashboard'),
    path('list/', ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('new/', ProjectCreateView.as_view(), name='project_new'),
]