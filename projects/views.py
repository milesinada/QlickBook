from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Project, Ticket
from django.shortcuts import render, redirect

# Create your views here.


def DashboardPageView(request):
  
    data_set = []
            # Get all the projects 
    
    project_list = Project.objects.all()
    
    for project in project_list:
        instance = {
            'count' : [0,0,0],
            'title' : project.title,
            'description' : project.description,
            'id' : project.id
            }            
        
        ticket_list = project.ticket_set.all()
# loop through each project and get all tickets associated with (this) projects
        for ticket in ticket_list:
            if ticket.status == 2:
                instance['count'][0] += 1
            elif ticket.status == 1:
                instance['count'][1] += 1
            elif ticket.status == 0:
                instance['count'][2] += 1
# loop through all tickets and count each status

# if statements for each status incrementing count

# after looping through all tickets we create an array of counts for the status

# append this count array to a temp dictionary
        data_set.append(instance)
  
    return render(request, 'dashboard.html', {'data_set': data_set})
      

def ProjectListView(request):  
    data_set = [] 
    project_list = Project.objects.all()    
    for project in project_list:
        instance = {
            'count' : [0,0,0],
            'title' : project.title,
            'description' : project.description,
            'id' : project.id
            }
        ticket_list = project.ticket_set.all()
        for ticket in ticket_list:
            if ticket.status == 2:
                instance['count'][0] += 1
            elif ticket.status == 1:
                instance['count'][1] += 1
            elif ticket.status == 0:
                instance['count'][2] += 1
        data_set.append(instance)  
    return render(request, 'projects/list.html', {'data_set': data_set})



# class ProjectListView(LoginRequiredMixin, ListView):
#     template_name = 'projects/list.html'
#     model = Project

class ProjectDetailView(LoginRequiredMixin, DetailView):
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

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "projects/edit.html"
    model = Project
    fields = '__all__'

    
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "projects/delete.html"
    model = Project
    success_url = "/projects"

class TicketListView(LoginRequiredMixin, ListView):
    template_name = 'tickets/ticket-list.html'
    model = Ticket

class TicketCreateView(LoginRequiredMixin, CreateView):
    template_name = "tickets/new.html"
    model = Ticket
    fields = ['title', 'author', 'dateCreated', 'dateResolved', 'difficulty', 'status', 'project', 'commentary']
    success_url = "/projects/{project_id}"

class TicketDetailView(LoginRequiredMixin, DetailView):
    template_name = "tickets/detail.html"
    model = Ticket
    success_url = "/projects/{project_id}"

    
def done(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.status = '2'
    ticket.save(update_fields=['status'])
    return request

    # project_id = Project.id
    # related_project = Ticket.project
    # # Project.objects.filter(id=self.kwargs['pk'])

    # project = Project.objects.filter(id=related_project)
    # # ticket_list = project.ticket_set.all()
    # context = {
    #     'project_id' : project,
    # }

    # form = TicketStatusForm()
    # Link a js file to the HTML and send a patch Request to the ticketupdateview

# def done(request, pk):
#     ticket = Ticket.objects.get(pk=pk)
#     project_id = ticket.project.id
#     return  redirect('project_detail', project_id)

class TicketUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "tickets/edit.html"
    model = Ticket
    fields = '__all__'
    success_url = "/projects/{project_id}"


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "tickets/delete.html"
    model = Ticket
    success_url = "/projects/{project_id}"
