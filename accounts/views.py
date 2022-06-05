from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    # form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class LoginPageView(TemplateView):
    template_name = 'registration/login.html'

class LoggedOutPageView(TemplateView):
    template_name = 'registration/logged_out.html'

class PasswordChangeFormPageView(TemplateView):
    template_name = 'registration/password_change_form.html'

class PasswordChangeDonePageView(TemplateView):
    template_name = 'registration/password_change_done.html'

class PasswordResetPageView(TemplateView):
    template_name = 'registration/password_reset.html'