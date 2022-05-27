from django.urls import path
from .views import SignUpPageView, LoginPageView, LoggedOutPageView, PasswordChangeFormPageView, PasswordChangeDonePageView, PasswordResetPageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignUpPageView.as_view(), name='signup'),    
    path('logged_out/', LoggedOutPageView.as_view(), name='logged_out'),
    path('password_change/', PasswordChangeFormPageView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDonePageView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetPageView.as_view(), name='password_reset'),

]