from rest_framework import generics
from school.models import Subject
from school.api.serializers import SubjectSerializer

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):
    queryset=Subject.objects.all()
    serializer_class = SubjectSerializer