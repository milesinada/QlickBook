from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=256)

    def __str__(self):
        return self.title