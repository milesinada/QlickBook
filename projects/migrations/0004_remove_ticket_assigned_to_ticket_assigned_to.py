# Generated by Django 4.0.4 on 2022-06-22 01:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_remove_ticket_assigned_to_ticket_assigned_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='ticket',
            name='assigned_to',
            field=models.ManyToManyField(related_name='assigned_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
