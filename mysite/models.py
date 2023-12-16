from django.db import models

# Create your models here.
class content(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255)
    massage = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ('created_date',) 

    def __str__(self):
        return self.name

class newsletter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email  