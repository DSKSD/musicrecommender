# coding: utf-8
from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name = 'index'), # 최초화면 / 타임라인!
    url(r'^post/(?P<pk>\d+)/$','main.views.PostView', name='post_detail'), # 포스팅 자세히 보기 (별점 매기고 유사한 아이템 추천 받는다)
    url(r'^accounts/register/$', views.register, name='register'), # 회원가입 POST 요청
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'), # 로그인 POST 요청
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name='logout'), # 로그아웃 요청
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'), 
    url(r'^post_delete/$', views.delete, name='post_delete'), # 포스팅 삭제 요청
    url(r'^newRating/$', views.newRating, name='new_rating'), # 별점 매기기 요청
    url(r'^loginForm/$', TemplateView.as_view(template_name='registration/login.html'), name='loginForm'), # 로그인 페이지 이동
    url(r'^registerForm/$', TemplateView.as_view(template_name='registration/registration_form.html'), name='registerForm'), # 회원가입 페이지 이동
    url(r'^search/$', views.query, name='search'),
    
]

if settings.DEBUG: # 개발 단계에서는 아래 Media url을 사용하겠다..!! 서비스 단에서는 S3 사용하고
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)