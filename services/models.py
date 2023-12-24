from django.db import models
from clients.models import ClientModel
from users.models import CustomUser
from attachments.models import Attachment
import uuid


class Type (models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    deadline_type = models.CharField(max_length=20, choices=[
        ('date_time_deadline', 'Data e Hora Marcada'),
        ('hours_deadline', 'Prazo em Horas'),
        ('scheduled_date', 'Agendamento para uma Data'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)


class Status(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Service (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE, related_name='client')
    subject = models.CharField(max_length=200, null=False, blank=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=False, blank=False, related_name='type')
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date_time_deadline = models.DateTimeField(blank=True, null=True)
    hours_deadline = models.IntegerField(blank=True, null=True)
    scheduled_date = models.DateField(blank=True, null=True)
    observation = models.TextField()
    attachment = models.ManyToManyField(Attachment, blank=True, related_name='attachment')
    finished = models.BooleanField(default=False)
    attendant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='service_attended')
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
