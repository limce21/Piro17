from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "posts"

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('post/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
    path('dev-create', views.create_devTool, name="dev-create"),
    path('dev/', views.home_devTool, name="dev-home"),
    path('tool/<int:id>', views.detail_devTool, name="dev-detail"),
    path("tool/delete/<int:id>", views.delete_devTool, name="dev-delete"),
    path('tool/update/<int:id>', views.update_devTool, name="dev-update"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
