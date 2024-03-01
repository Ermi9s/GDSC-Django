from django.db import models
from Blog.models import Post

# Create your models here.

class Comment(models.Model):
    Content = models.CharField(max_length = 100)
    Author = models.CharField(max_length = 100)
    Published_Date = models.DateTimeField(auto_now = True)
    post = models.ForeignKey(Post , on_delete = models.CASCADE)
    
    def __str__(self) -> str:
        return self.Content
