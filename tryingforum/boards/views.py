from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.
def home(request):
    brs = Board.objects.all()
    return render(request,'boards/home.html',{'brs':brs})
