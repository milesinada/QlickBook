from django.views.generic import TemplateView, ListView, DetailView
from .models import Project

# Create your views here.
class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

class ProjectListView(ListView):
    template_name = 'projects/list.html'
    model = Project

class ProjectDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = Project