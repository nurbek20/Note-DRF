from django.shortcuts import render, get_object_or_404
from main.models import Note
# Create your views here.
from main.serializers import NoteSerializer
from rest_framework.viewsets import ModelViewSet
 

class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer

    def get_object(self):
        return get_object_or_404(Note, pk=self.request.query_params.get('id'))


    def get_queryset(self):
        return Note.objects.all()