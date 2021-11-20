from django.contrib import admin
from .models import AddPost

# Register your models here.
class AdminPost(admin.ModelAdmin):
     list_display = [
         'author',
         'blog_title',
         'blog_image',
         'blog_content'
     ]
admin.site.register(AddPost,AdminPost)
