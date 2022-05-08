from django.views.generic import TemplateView, ListView, DetailView
from django.views.edit import CreateView
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

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "projects/new.html"
    model = Project
    fields = ['title', 'description']