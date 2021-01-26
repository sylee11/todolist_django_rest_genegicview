from django.shortcuts import render
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
# Create your views here.

class TaskView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


class TaskUpdate(generics.UpdateAPIView):
    lookup_field = 'id'
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = request.data.get("status")
        instance.save()
        return Response('oke')

class TaskAdd(generics.CreateAPIView):
    serializer_class = TaskSerializer



