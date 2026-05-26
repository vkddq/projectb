from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Branch
from .serializers import BranchSerializer

def home_view(request):
    branches = Branch.objects.all()
    return render(request, 'home.html', {'branches': branches})

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated]