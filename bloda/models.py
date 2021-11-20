from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class AddPost(models.Model):
     author = models.ForeignKey(User,on_delete = models.CASCADE)
     blog_image = models.ImageField(null=True, blank=True, upload_to="img/")
     blog_title = models.CharField(max_length=20)
     blog_content = models.TextField(max_length = 500)

     def __str__(self):
          return self.blog_title
