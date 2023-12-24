from rest_framework import generics
from .models import ClientModel
from .serializers import ClientSerializer


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
