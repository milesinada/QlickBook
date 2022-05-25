from django.urls import path

from projects.views import TicketListView
from .views import (
    DashboardPageView,
    ProjectListView, 
    ProjectDetailView, 
    ProjectCreateView, 
    TicketCreateView,
    TicketListView,
)

urlpatterns = [
    path('', DashboardPageView.as_view(), name='dashboard'),
    path('list/', ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('new-project/', ProjectCreateView.as_view(), name='project_new'),
    path('new-ticket/', TicketCreateView.as_view(), name='ticket_new'),
    path('tickets/', TicketListView.as_view(), name='ticket_list'),

]