from django.db import models

# Create your models here.
class Post(models.Model):
    #author
    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.IntegerField(default=0)
    #image
    #category
    status = models.BooleanField(default=False)
    #tag
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
