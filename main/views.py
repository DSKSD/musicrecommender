# coding: utf-8
# Create your views here.
from django.contrib.auth import authenticate, login as _login
from django.http import HttpResponseRedirect
from .models import Post, Vote
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

# 회원가입 및 로그인 구현 부분 
from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.core.context_processors import csrf
from django.contrib.auth import get_user_model


def register(request):
     if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             return render_to_response('registration/registration_complete.html')

     else:
         form = UserCreationForm()
     token = {}
     token.update(csrf(request))
     token['form'] = form

     return render_to_response('registration/registration_form.html', token)



def loggedin(request):
    return render_to_response('registration/loggedin.html',{'username': request.user.username})

############


def index(request):
    user = request.user
    posts = Post.objects.all().order_by('-published_date')
    
    context = {'posts' : posts, 'current_user' : user,}
    return render(request, 'main/index.html', context)

def PostView(request,pk=None):
    object1=Post.objects.get(id=int(pk))
    username= request.user
    try:
        vote = Vote.objects.get(user=username.id, post = object1.id)
        voteRating = vote.score
    except:
        voteRating = 0
    return render(request, 'main/post_detail.html',{'object':object1, 'voteRating': voteRating, 'current_user' : username,})


def delete(request):
    pid = request.POST['id_of_post']
    post = get_object_or_404(Post, pk=pid)
    post.delete()
    
    return redirect('main.views.index')
    

def newRating(request):
    
    username = request.user
    post = request.POST['post']
    try:
        vote = Vote.objects.get(user=username.id, post = post)
        vote.score = request.POST['scoring']
        vote.save()
        return redirect('main.views.PostView', pk=post)
    except:
        vote = Vote()
        vote.user = username
        vote.post_id = post
        vote.site_id = 1
        vote.score = request.POST['scoring']
        vote.save()
    
    return redirect('main.views.PostView', pk=post)