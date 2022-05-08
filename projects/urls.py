from django.urls import path
<<<<<<< HEAD
from .views import DashboardPageView, ProjectListView, ProjectCreateView
=======
from .views import DashboardPageView, ProjectListView, ProjectDetailView
>>>>>>> 3bdaa7efadb13bae6e0bd5a32da000214d6e3ae3

urlpatterns = [
    path('', DashboardPageView.as_view(), name='dashboard'),
    path('list/', ProjectListView.as_view(), name='project_list'),
<<<<<<< HEAD
    path('new/', ProjectCreateView.as_view(), name='project_new'),
=======
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
>>>>>>> 3bdaa7efadb13bae6e0bd5a32da000214d6e3ae3
]