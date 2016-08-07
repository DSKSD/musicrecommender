from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^post/(?P<pk>\d+)/$','main.views.PostView', name='post_detail'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^post_delete/$', views.delete, name='post_delete'),
    url(r'^newRating/$', views.newRating, name='new_rating'),
    url(r'^loginForm/$', TemplateView.as_view(template_name='registration/login.html'), name='loginForm'),
    url(r'^registerForm/$', TemplateView.as_view(template_name='registration/registration_form.html'), name='registerForm'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)