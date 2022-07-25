from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


appname='pirostagrams'

urlpatterns = [
   path('', views.post, name="post"),
   path('like_ajax/', views.like_ajax, name='like_ajax'),
   path('register_comment/', views.register_comment, name='register_comment'),
   path('delete_comment/', views.delete_comment, name='delete_comment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)