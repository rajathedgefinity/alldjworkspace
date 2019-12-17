from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Board

# Create your views here.
def home(request):
    brs = Board.objects.all()
    return render(request,'boards/home.html',{'brs':brs})

def board_topics(request, pk):
    br = get_object_or_404(Board, pk=pk)
    return render(request,'boards/topics.html', {'br':br})
