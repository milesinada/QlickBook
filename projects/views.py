<<<<<<< HEAD
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic.edit import CreateView
=======
from django.views.generic import TemplateView, ListView, DetailView
>>>>>>> 3bdaa7efadb13bae6e0bd5a32da000214d6e3ae3
from .models import Project

# Create your views here.
class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

class ProjectListView(ListView):
    template_name = 'projects/list.html'
    model = Project

<<<<<<< HEAD
class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "projects/new.html"
    model = Project
    fields = ['title', 'description']
=======
class ProjectDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = Project
>>>>>>> 3bdaa7efadb13bae6e0bd5a32da000214d6e3ae3
