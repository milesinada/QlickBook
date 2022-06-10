from django.urls import include, path
from . import views

from .views import (
    DashboardPageView,
    ProjectListView, 
    ProjectDetailView, 
    ProjectCreateView, 
    ProjectUpdateView,
    ProjectDeleteView, 
    TicketCreateView,
    TicketListView,
    TicketDeleteView,
    TicketDetailView,
    TicketUpdateView,
    done,
    
)

urlpatterns = [
    path('', DashboardPageView, name='dashboard'),
    path('list/', ProjectListView, name='project_list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('new-project/', ProjectCreateView.as_view(), name='project_new'),
    path('<int:pk>/edit-project/', ProjectUpdateView.as_view(), name='project_edit'),
    path('<int:pk>/delete-project/', ProjectDeleteView.as_view(), name='project_delete'),
    path('new-ticket/', TicketCreateView.as_view(), name='ticket_new'),
    path('tickets/', TicketListView.as_view(), name='ticket_list'),
    path('<int:pk>/ticket/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<int:pk>/edit-ticket/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('<int:pk>/delete-ticket/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('done/<int:pk>', done, name='done'),

]