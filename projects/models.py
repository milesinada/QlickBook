from multiprocessing import AuthenticationError
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=256)
    
    def __str__(self):
        return self.title

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

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateResolved = models.DateTimeField()
    difficulty = models.IntegerField(default=DifficultyLevel.EASY, choices=DifficultyLevel.choices)
    status = models.IntegerField(default=StatusLevel.NOTSTARTED, choices=StatusLevel.choices)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    commentary = models.TextField(max_length=256)
    
    def __str__(self):
        return self.title