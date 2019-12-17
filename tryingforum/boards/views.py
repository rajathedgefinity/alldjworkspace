from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Board

# Create your views here.
def home(request):
    brs = Board.objects.all()
    return render(request,'boards/home.html',{'brs':brs})

def board_topics(request, pk):
    try:
        br = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request,'boards/topics.html', {'br':br})
