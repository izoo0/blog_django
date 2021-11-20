from django.forms import ModelForm
from .models import AddPost

class Post(ModelForm):
     class Meta:
          model = AddPost
          fields = ('author','blog_title','blog_image','blog_content',)