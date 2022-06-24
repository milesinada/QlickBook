from multiprocessing import context
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime



# from .forms import UserChoiceForm
from .models import Project, Ticket, Sprint
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.apps import apps
CustomUser = apps.get_model('accounts', 'CustomUser')


@login_required
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
        # loop through all tickets and count each status
        # if statements for each status incrementing count
            if ticket.status == 2:
            # after looping through all tickets we create an array of counts for the status
                instance['count'][0] += 1
            elif ticket.status == 1:
                instance['count'][1] += 1
            elif ticket.status == 0:
                instance['count'][2] += 1
        # append this count array to a temp dictionary
        data_set.append(instance)  
    return render(request, 'dashboard.html', {'data_set': data_set})

#------------------- Project Views -----------------------------

@login_required
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

def ProjectDetailView(request, pk):
    project = Project.objects.get(pk=pk)
    ticket_list = project.ticket_set.all()
    sprint_list = project.sprint_set.all()
    instance = {
            'count' : [0,0,0],
            'title' : project.title,
            'description' : project.description,
            'id' : project.id,
            'ticket_list' : ticket_list,
            'sprint_list' : sprint_list
            }
    for ticket in ticket_list:
        if ticket.status == 2:
            instance['count'][0] += 1
        elif ticket.status == 1:
            instance['count'][1] += 1
        elif ticket.status == 0:
            instance['count'][2] += 1

    
    # assign the tickets to every sprint  
    sprint_list_with_tasks = []
    for sprint in sprint_list:
        print(sprint.title)
        sprint_tickets = Ticket.objects.filter(sprint=sprint)
        record = { "sprint": sprint }
        record["tickets"] = sprint_tickets
        sprint_list_with_tasks.append(record)
    

    instance["sprints_tasks"] = sprint_list_with_tasks

    # data_count = instance.count[0]
    # print(data_count)
    return render(request, 'projects/detail.html', instance)

# class ProjectDetailView(LoginRequiredMixin, DetailView):
#     model = Project
#     template_name = 'projects/detail.html'
#     def get_queryset(self):
#         return Project.objects.filter(id=self.kwargs['pk'])
#     
#     def get_context_data(self, **kwargs):
#         context = super(ProjectDetailView, self).get_context_data(**kwargs)
#         context["ticket_list"] = Ticket.objects.filter(project_id=self.kwargs['pk'])
#         return context
#         # select_related used if only need 1 query to server. would be better to use in ticket_detail rather Project detail. In Ticket_detail to show Project.title use S_R()

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
    success_url = "/projects/list"


#------------------- Ticket Views -----------------------------

@login_required
def done(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.dateResolved = datetime.now()
    ticket.status = '2'
    ticket.milestone_resolved = ticket.sprint.milestone
    ticket.save(update_fields=['status','dateResolved','milestone_resolved'])
    return redirect(reverse('ticket_detail', kwargs={'pk':ticket.pk}))
    # project= ticket.project.id
    # return redirect(reverse('project_detail', kwargs={'pk':project}))

@login_required
def progress(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.status = '1'
    ticket.dateResolved = None
    ticket.save(update_fields=['status','dateResolved'])
    project= ticket.project.id
    # return redirect(reverse('project_detail', kwargs={'pk':project})) #This works to redir to project!!
    return redirect(reverse('ticket_detail', kwargs={'pk':ticket.pk}))  #This works without refresh in ticket detail!!

@login_required
def assign_users(request,pk):    
    ticket = Ticket.objects.get(pk=pk)
    # ticket.assigned_to = []
    for user_name in request.POST.getlist('assigned_to'):
        print(user_name)
        user_object = CustomUser.objects.filter(username=user_name).first()
        # get the user 
        ticket.assigned_to.add(user_object)
        #add instead of appedn because it's a model not a list
    
    ticket.save()
    return redirect(reverse('ticket_detail', kwargs={'pk':ticket.pk}))

@login_required
def unassign_users(request,pk):    
    ticket = Ticket.objects.get(pk=pk)
    for user_name in request.POST.getlist('assigned_to'):
        print(user_name)
        user_object = CustomUser.objects.filter(username=user_name).first()
        # get the user 
        ticket.assigned_to.remove(user_object)
        #remove instead of add because it's reverse logic
    
    ticket.save()
    return redirect(reverse('ticket_detail', kwargs={'pk':ticket.pk}))

class TicketListView(LoginRequiredMixin, ListView):
    template_name = 'tickets/ticket-list.html'
    model = Ticket

class TicketCreateView(LoginRequiredMixin, CreateView):
    template_name = "tickets/new.html"
    model = Ticket
    # form = UserChoiceForm
    fields = ['title','author','dateCreated','difficulty','project','commentary']
    success_url = "/projects/{project_id}"
    # CustomUser = get_user_model()
    # user_list = CustomUser.objects.values()

    # usernames = CustomUser_values.username
    # def get_context_data(self, **kwargs):
    #     CustomUser = get_user_model()
    #     context = super(TicketCreateView, self).get_context_data(**kwargs)
    #     context['username'] = CustomUser.objects.values()    
    #     return context
    # def get_usernames():
    #     CustomUser = get_user_model()
    #     User_list = CustomUser.objects.get()
    #     for username in User_list:
    #         print(username)
    
    # username = user_list
    # print(username)
    # print(username)

# def TicketDetailView(request, pk):
#     ticket = Ticket.objects.get(pk=pk)
#     users = CustomUser.objects.all()
#     user_list = users.all()
#     instance = {
#             'user_list' : user_list
#             }
#     return render(request, 'tickets/detail.html', instance)

class TicketDetailView(LoginRequiredMixin, DetailView):
    template_name = "tickets/detail.html"
    model = Ticket  
    # form = UserChoiceForm
    CustomUser = get_user_model()
    # assigned_users = Ticket.assigned_to
    # for user_assigned in ticket.assigned_to.all():
    #     print(user_assigned)
    # for assigned_users in assigned:
    # users_list = users_set.all()
    # print(Ticket.assigned_to)
    # print(users_set)

    # def get_user_list(self, request):
    #     users_set = CustomUser.objects.all()
    #     instance = {
    #         'users_set': users_set
    #             }
    #     return render(request, 'tickets/detail.html', instance)



    def get_context_data(self, **kwargs):
            CustomUser = get_user_model()
            context = super(TicketDetailView, self).get_context_data(**kwargs)
            context['username'] = CustomUser.objects.values()    
            context["all_users"] = CustomUser.objects.all()
            return context


    # Make a function to complete a Ticket. Function based done()
    # def done(request, pk):
    #     ticket = Ticket.objects.get(pk=pk)
    #     project_id = ticket.project.id
    #     return  redirect('project_detail', project_id)

class TicketUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "tickets/edit.html"
    model = Ticket
    fields = ['title', 'author', 'dateCreated', 'dateResolved', 'sprint', 'project', 'difficulty', 'status', 'commentary']
    success_url = "/projects/{project_id}"


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "tickets/delete.html"
    model = Ticket
    success_url = "/projects/{project_id}"

#------------------- Sprints Views -----------------------------

@login_required
def assign_tickets(request,pk):    
    sprint = Sprint.objects.get(pk=pk)
    # ticket.assigned_to = []
    for ticket in request.POST.getlist('tickets'):
        ticket_object = Ticket.objects.filter(title=ticket).first()
        # get the user 
        ticket_object.sprint = sprint
        #add instead of appedn because it's a model not a list
    
    ticket_object.save()
    return redirect(reverse('sprint_detail', kwargs={'pk':sprint.pk}))

@login_required
def unassign_tickets(request,pk):    
    sprint = Sprint.objects.get(pk=pk)
    for ticket in request.POST.getlist('tickets'):
        ticket_object = Ticket.objects.filter(title=ticket).first()
        # get the user 
        ticket_object.sprint = None
        #remove instead of add because it's reverse logic
    
    ticket_object.save()
    return redirect(reverse('sprint_detail', kwargs={'pk':sprint.pk}))

@login_required
def next_milestone(request,pk):
    sprint = Sprint.objects.get(pk=pk)
    sprint.milestone += 1
    # next = current+1
    # current = sprint.next
    sprint.save(update_fields=['milestone'])
    return redirect(reverse('sprint_detail', kwargs={'pk':sprint.pk})) 

class SprintListView(LoginRequiredMixin,ListView):
    template_name = "sprints/list.html"
    model = Sprint
    

# @login_required
# def SprintListView(request):
#     sprint_list = Sprint.objects.all()
#     sprint_list_with_tasks = []
#     for sprint in sprint_list:
#         print(sprint.title)
#         sprint_tickets = Ticket.objects.filter(sprint=sprint)
#         record = { "sprint": sprint }
#         record["tickets"] = sprint_tickets
#         sprint_list_with_tasks.append(record)
    
#     instance = {
#         'count' : [0,0,0],
#         'title' : sprint.title,
#         'id' : sprint.id,
#         'sprint_list' : sprint_list
#         }

#     instance["sprints_tasks"] = sprint_list_with_tasks

#     # data_count = instance.count[0]
#     # print(data_count)
#     return render(request, 'sprints/list.html', instance)

class SprintCreateView(LoginRequiredMixin, CreateView):
    template_name = "sprints/new.html"
    model = Sprint
    fields = '__all__'
    success_url = "/projects/sprints"

class SprintDetailView(LoginRequiredMixin, DetailView):
    template_name = "sprints/detail.html"
    model = Sprint  

    def get_queryset(self):
        return Sprint.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(SprintDetailView, self).get_context_data(**kwargs)
        context["ticket_list"] = Ticket.objects.filter(sprint_id=self.kwargs['pk'])
        context["project_tickets"] = Ticket.objects.filter(project_id=self.kwargs['pk'])
        context['complete_milestones'] = []
        sprint = Sprint.objects.get(id=self.kwargs['pk'])
        for n in range(1,sprint.milestone+1):
            completed = Ticket.objects.filter(milestone_resolved=n,sprint_id=sprint.id).count()
            item = {
                'number' : n,
                'tickets' : completed, 
            }
            context['complete_milestones'].append(item)
        return context

    # Need to have a list of Tickets and correlating Project

class SprintUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "sprints/edit.html"
    model = Sprint
    fields = '__all__'
    success_url = "/projects/{id}/sprint"



class SprintDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "sprints/delete.html"
    model = Sprint
    success_url = "/projects/{project_id}"
