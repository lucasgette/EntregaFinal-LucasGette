
from django import forms
from django.contrib.auth.models import User
from .models import Blog, Comments
from ckeditor.fields import RichTextFormField



class CrearPost(forms.ModelForm):
    
    body = RichTextFormField(required=True)

    class Meta:
        model = Blog
        fields = ['title','subtitle','body', 'blog_image', 'calification']
        help_texts = {k:'' for k in fields }


class PostSearch(forms.Form):
    title = forms.CharField(max_length=60, label='Titulo del post')


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ['comment']

