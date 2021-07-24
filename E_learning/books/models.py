from django.db import models

# Create your models here.

class Books(models.Model):
    'This is the class models for books'

    Title = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Isbn_no = models.CharField(max_length=100)
    File = models.FileField(upload_to='covers/',blank=True)
    

    def __str__(self):
        return self.title
