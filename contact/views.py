from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, ListCreateAPIView, DestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.
class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactCreateAPIView(CreateAPIView):
    # queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactUpdateApiView(UpdateAPIView):
    lookup_field = 'pk'
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class DeleteApiView(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

@api_view(http_method_names=['POST'])
def test(request):
    print(request.data)
    a = [2,3,4,5]
    print(JSONRenderer().render(a))
    return Response(request.data)