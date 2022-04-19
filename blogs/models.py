from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(null=True, blank=True)
    blog_image = models.ImageField(upload_to='blogs/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    calification = models.IntegerField(        
        validators=[MinValueValidator(0), 
                    MaxValueValidator(10)])

    def __str__(self):
        return f'{self.title} - {self.author} - {self.date} '




class Comments(models.Model):
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.commentator.username + ' | ' + str(self.date) + ' | ' + self.post.title