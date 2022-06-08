from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Project, Ticket
from django.shortcuts import render
# from .forms import TicketStatusForm

# Create your views here.
def DashboardPageView(request):
  
    data_set = []
            # Get all the projects 
    
    project_list = Project.objects.all()
    
    for project in project_list:
        instance = {
            'count' : [0,0],
            'title' : project.title,
            'description' : project.description,
            'id' : project.id
            }
        
        
        
        ticket_list = project.ticket_set.all()
# loop through each project and get all tickets associated with (this) projects
        for ticket in ticket_list:
            if ticket.status == 0:
                instance['count'][0] += 1
            elif ticket.status == 1:
                instance['count'][1] += 1
# loop through all tickets and count each status

# if statements for each status incrementing count

# after looping through all tickets we create an array of counts for the status

# append this count array to a temp dictionary
        data_set.append(instance)
  
    return render(request, 'dashboard.html', {'data_set': data_set})


# class DashboardPageView(ListView):
#     template_name = 'dashboard.html'
#     model = Project
  
        


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
    # form = TicketStatusForm()
    # Link a js file to the HTML and send a patch Request to the ticketupdateview

# def done(request, pk):
#     ticket = Ticket.objects.get(pk=pk)
#     project_id = Ticket.Project.id
#     return redirect ('project_detail', project_id)

class TicketUpdateView(UpdateView):
    template_name = "tickets/edit.html"
    model = Ticket
    fields = ['title', 'author', 'dateCreated', 'dateResolved', 'difficulty', 'status', 'project', 'commentary']

class TicketDeleteView(DeleteView):
    template_name = "tickets/delete.html"
    model = Ticket
    success_url = reverse_lazy('project_detail')
