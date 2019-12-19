from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    brs = Board.objects.all()
    return render(request,'boards/home.html',{'brs':brs})

def board_topics(request, pk):
    br = get_object_or_404(Board, pk=pk)
    return render(request,'boards/topics.html', {'br':br})

def new_topic(request, pk):
    br = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()

        topic = Topic.objects.create(subject=subject,board=br,starter=user)
        post = Post.objects.create(message=message, topic=topic, created_by=user)

        return redirect('board_topics',pk=br.pk)
    return render(request, 'boards/new_topic.html',{'br':br})
