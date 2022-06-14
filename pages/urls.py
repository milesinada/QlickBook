from django.urls import path
from .views import HomePageView, AboutPageView, TicketHistoryPageView, FaqPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('ticket-history/', TicketHistoryPageView.as_view(), name='ticket-history'),
    path('faq/', FaqPageView.as_view(), name='faq'),
    path('contact/', ContactPageView.as_view(), name='contact'),

]