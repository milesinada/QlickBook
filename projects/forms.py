from django import forms

class ViewForm(forms.Form):
    statuses = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]
    status = forms.ChoiceField(label='Status', required=True, choices=statuses, widget=forms.Select(attrs={'onchange': 'actionform.submit()'}))