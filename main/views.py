# coding: utf-8
# Create your views here.
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login as _login
from django.http import HttpResponseRedirect
from .models import Post, Vote
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
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
    posts = Post.objects.all().order_by('-meanstar') # 평균 별점에 내림차순으로 정렬
    newthings = Post.objects.all().order_by('-published_date')[:5] # 등록된 순으로 5개 뽑음
    context = {'posts' : posts, 'current_user' : user, 'newthings' : newthings,}
    return render(request, 'main/index.html', context)

# 자세히 보기 {자세히 보려는 Post , 별점 정보, 현재 유저 }
def PostView(request,pk=None):
    object1=Post.objects.get(id=int(pk))
    username= request.user
    # 이미 이 유저가 이 post에 대해 Rating한 적이 있다면 voteRating에 그 vote instance를 담고 아니라면 0을 담아라 
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
    post = request.POST['post'] # Rating을 매길 post의 pk 
    # 이미 Rating을 매긴적이 있다면 그 Vote 인스턴스를 찾아서 score만 수정해주고 
    try:
        vote = Vote.objects.get(user=username.id, post = post)
        vote.score = request.POST['scoring']
        vote.save()
        return redirect('main.views.PostView', pk=post)
    # 아예 처음 Rating 매기는거라면 vote 인스턴스를 새로 생성해서 score를 넣어준다. 
    except:
        vote = Vote()
        vote.user = username
        vote.post_id = post
        vote.site_id = 1
        vote.score = request.POST['scoring']
        vote.save()
    
    return redirect('main.views.PostView', pk=post)


    
def query(request):
    qry = request.GET['query']
    objects = Post.objects.filter(Q(title__icontains=qry) | Q(text__icontains=qry) | Q(artist__icontains=qry) | Q(songname__icontains=qry))
    context = {'query' : qry, 'objects' : objects,}
    
    return  render(request, 'main/search.html', context)