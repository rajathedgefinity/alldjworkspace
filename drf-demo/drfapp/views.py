from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, University
from .serializers import UniversitySerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
