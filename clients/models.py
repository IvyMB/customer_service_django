from django.db import models
from core.models import Country, Gender, State
import uuid


class ClientModel (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    birthday = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='client_gender')
    address = models.CharField(max_length=500)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='client_state')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='client_country')
    document = models.CharField(max_length=20, blank=True, null=True, unique=True)
    telephone1 = models.CharField(max_length=15)
    telephone2 = models.CharField(max_length=15)
    created_at = models.DateTimeField()
