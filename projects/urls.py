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
    SprintDeleteView,
    SprintUpdateView,
    SprintCreateView,
    SprintDetailView,
    SprintListView,
    done,
    assign_users,
    unassign_users,
    progress,
)

urlpatterns = [
    path('', views.DashboardPageView, name='dashboard'),
    # Projects
    path('list/', views.ProjectListView, name='project_list'),
    path('<int:pk>/', ProjectDetailView, name='project_detail'),
    path('new-project/', ProjectCreateView.as_view(), name='project_new'),
    path('<int:pk>/edit-project/', ProjectUpdateView.as_view(), name='project_edit'),
    path('<int:pk>/delete-project/', ProjectDeleteView.as_view(), name='project_delete'),
    # Tickets
    path('new-ticket/', TicketCreateView.as_view(), name='ticket_new'),
    path('tickets/', TicketListView.as_view(), name='ticket_list'),
    path('<int:pk>/ticket/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<int:pk>/edit-ticket/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('<int:pk>/delete-ticket/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('done/<int:pk>', done, name='complete_status'),
    path('progress/<int:pk>', progress, name='progress_status'),
    path('users/<int:pk>', assign_users, name='assign_users'),
    path('unassign/<int:pk>', unassign_users, name='unassign_users'),
    # Sprints
    path('sprints/', SprintListView.as_view(), name='sprint_list'),
    path('<int:pk>/sprint', SprintDetailView.as_view(), name='sprint_detail'),
    path('new-sprint/', SprintCreateView.as_view(), name='sprint_new'),
    path('<int:pk>/edit-sprint/', SprintUpdateView.as_view(), name='sprint_edit'),
    path('<int:pk>/delete-sprint/', SprintDeleteView.as_view(), name='sprint_delete'),

]