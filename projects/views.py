from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic.edit import CreateView
from .models import Project

# Create your views here.
class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

class ProjectListView(ListView):
    template_name = 'projects/list.html'
    model = Project

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "projects/new.html"
    model = Project
    fields = ['title', 'description']