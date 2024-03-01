from django.db import models

class Post(models.Model):
    Title = models.CharField(max_length = 100 , unique = True)
    Content = models.TextField()
    Catagory = models.CharField(max_length = 100)
    Image = models.ImageField()
    Tags = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.Title