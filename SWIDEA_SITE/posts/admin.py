from django.contrib import admin
from .models import Post, DevTool

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(DevTool)
class DevToolAdmin(admin.ModelAdmin):
    pass