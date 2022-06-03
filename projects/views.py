from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Project, Ticket

# Create your views here.
class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

class ProjectListView(ListView):
    template_name = 'projects/list.html'
    model = Project

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'
    def get_queryset(self):
        return Project.objects.filter(id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context["ticket_list"] = Ticket.objects.filter(project_id=self.kwargs['pk'])
        return context
        # select_related used if only need 1 query to server. would be better to use in ticket_detail rather Project detail. In Ticket_detail to show Project.title use S_R()

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "projects/new.html"
    model = Project
    fields = ['title', 'description']

class TicketListView(ListView):
    template_name = 'tickets/ticket-list.html'
    model = Ticket

class TicketCreateView(LoginRequiredMixin, CreateView):
    template_name = "tickets/new.html"
    model = Ticket
    fields = ['title', 'author', 'dateCreated', 'dateResolved', 'difficulty', 'status', 'project', 'commentary']

class TicketDetailView(DetailView):
    template_name = "tickets/detail.html"
    model = Ticket

class TicketUpdateView(UpdateView):
    template_name = "tickets/edit.html"
    model = Ticket
    fields = ['title', 'author', 'dateCreated', 'dateResolved', 'difficulty', 'status', 'project', 'commentary']

class TicketDeleteView(DeleteView):
    template_name = "tickets/delete.html"
    model = Ticket
    success_url = reverse_lazy('project_list')

