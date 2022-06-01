from django.views.generic import TemplateView, ListView
from projects.models import Ticket

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class TicketHistoryPageView(ListView):
    model = Ticket
    template_name = 'ticket-history.html'

class FaqPageView(TemplateView):
    template_name = 'faq.html'