from django.urls import path

from .views import (
    DashboardPageView,
    ProjectListView, 
    ProjectDetailView, 
    ProjectCreateView, 
    TicketCreateView,
    TicketListView,
    TicketDeleteView,
    TicketDetailView,
    TicketUpdateView
)

urlpatterns = [
    path('', DashboardPageView, name='dashboard'),
    path('list/', ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/',
        ProjectDetailView.as_view(), name='project_detail'),
    path('new-project/', ProjectCreateView.as_view(), name='project_new'),
    path('new-ticket/', TicketCreateView.as_view(), name='ticket_new'),
    path('tickets/', TicketListView.as_view(), name='ticket_list'),
    path('<int:pk>/ticket/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<int:pk>/edit-ticket/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('<int:pk>/delete-ticket/', TicketDeleteView.as_view(), name='ticket_delete'),

]