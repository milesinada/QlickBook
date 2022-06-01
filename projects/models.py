from multiprocessing import AuthenticationError
from time import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone




# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=256)
    def __str__(self):
        return self.title
#Querey set foreignkey from ticket ORM Done in the views, pull search related (?)
class Ticket(models.Model):
    title = models.CharField(max_length=20)
    
    class DifficultyLevel(models.IntegerChoices):
        EASY = 0, ('Easy')
        NORMAL = 1, ('Normal')
        HARD = 2, ('HARD')

    class StatusLevel(models.IntegerChoices):
        NOTSTARTED = 0, ('Not Started')
        PROGRESS = 1, ('In Progress')
        COMPLETED = 2, ('Completed')

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    dateCreated = models.DateTimeField(default=timezone.now)
    dateResolved = models.DateField(null=True, blank=True)
    difficulty = models.IntegerField(default=DifficultyLevel.EASY, choices=DifficultyLevel.choices)
    status = models.IntegerField(default=StatusLevel.NOTSTARTED, choices=StatusLevel.choices)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    commentary = models.TextField(max_length=256)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_list')