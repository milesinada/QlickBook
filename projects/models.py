from email.policy import default
from multiprocessing import AuthenticationError
from time import timezone
from django.db import models 
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
# from accounts.models import CustomUser




# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=256)
    # users = models.ManyToManyField(CustomUser)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('project_list')

#Querey set foreignkey from ticket ORM Done in the views, pull search related (?)


class Sprint(models.Model):

    class Milestone(models.IntegerChoices):
        FIRST = 1, ('First')
        SECOND = 2, ('Second')
        THIRD = 3, ('Third')
        FINAL = 4, ('Final')

    LENGTH_CHOICES = (('1_week', '1 Week'), ('2_weeks', '2 Weeks'), ('3_weeks', '3 Weeks'))
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="sprints", null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now = False, auto_now_add=False)
    end_date = models.DateField(auto_now = False, auto_now_add=False)
    duration = models.CharField(max_length = 10, choices = LENGTH_CHOICES)
    complete = models.BooleanField(null=True, default=False)
    retrospective = models.CharField(max_length=10000, blank=True, null=True)
    milestone = models.IntegerField(default=Milestone.FIRST, choices=Milestone.choices)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    class DifficultyLevel(models.IntegerChoices):
        ENTRY = 0, ('Entry')
        JUNIOR = 1, ('Junior')
        MID = 2, ('Mid')
        SENIOR = 3, ('Senior')
        LEAD = 4, ('Lead')
    class StatusLevel(models.IntegerChoices):
        NOTSTARTED = 0, ('Not Started')
        PROGRESS = 1, ('In Progress')
        COMPLETED = 2, ('Completed')
    title = models.CharField(max_length=20)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(default=timezone.now)
    dateResolved = models.DateTimeField(blank = True, null=True)
    milestone_resolved = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=DifficultyLevel.ENTRY, choices=DifficultyLevel.choices)
    status = models.IntegerField(default=StatusLevel.NOTSTARTED, choices=StatusLevel.choices)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True)
    commentary = models.TextField(max_length=256)

    assigned_to = models.ManyToManyField(get_user_model(), related_name='assigned_users')
    
    #if complete status(2) is updated, dateResolved should be updated

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_list')

    
