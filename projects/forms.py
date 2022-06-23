# import enum
# from django import forms
# # from accounts.models import CustomUser

# # from django.apps import apps
# # CustomUser = apps.get_model('accounts', 'CustomUser')
# from django.contrib.auth import get_user_model



# class UserChoiceForm(forms.Form):
#     CustomUser = get_user_model()
#     USER_CHOICES = [[CustomUser.username, CustomUser.first_name ] for CustomUser in CustomUser.objects.all()]
#     assignees = forms.MultipleChoiceField(choices=USER_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False)