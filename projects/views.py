from django.views.generic import TemplateView

# Create your views here.
class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'