from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin 
from projects.models import Ticket

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class TicketHistoryPageView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'ticket-history.html'

class FaqPageView(TemplateView):
    template_name = 'faq.html'