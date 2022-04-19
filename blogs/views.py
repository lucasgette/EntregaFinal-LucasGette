from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import CrearPost, PostSearch, CommentForm
from index.forms import ConfirmationForm
from .models import Blog, Comments
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView


# Create your views here.


# Crear, Borrar, Editar y ver detalles

@login_required
def new_post(request):
    if request.method == 'POST':
        blog_form = CrearPost(request.POST, request.FILES)
        if blog_form.is_valid():
            data = blog_form.cleaned_data
            author = request.user
            new_blog = Blog(author=author,title=data['title'],subtitle=data['subtitle'],body=data['body'],blog_image=data['blog_image'],calification=data['calification'])
            new_blog.save()
            return redirect('my_profile')    

        else:
            return render(request, 'create_blog.html', {'blog_form':blog_form, 'msj':'Datos con formato incorrecto'} )            
        
    else:
        blog_form = CrearPost()
        context = {
            'blog_form':blog_form,
        }
        return render(request,'create_blog.html',context)

@login_required
def delete_post(request, pk):
    post = Blog.objects.get(pk=pk)

    if post.author == request.user:
        if request.method == 'POST':
            confirmation = ConfirmationForm(request.POST)

            if confirmation.is_valid():
                data = confirmation.cleaned_data
                if data['confirmation']:
                    post.delete()
                    return redirect('my_profile')
                
        else:
            confirmation = ConfirmationForm()

            context = {
                'confirmation': confirmation,
                'post':post
            }

            return render(request,'delete_post.html', context)

    else:
        return redirect('home')

@login_required
def edit_post(request, pk):
    post = Blog.objects.get(pk=pk)
    author = post.author

    # AGREGAR LA LOGICA A EDITAR

    if author == request.user:
        if request.method == 'POST':
            blog_form = CrearPost(request.POST, request.FILES, instance=post)
            if blog_form.is_valid():
                blog_form.save()
                return redirect('my_profile')

        else:
            blog_form = CrearPost(instance=post)
            
            context = {
                'blog_form':blog_form
            }
            return render(request,'edit_post.html', context)

    else:
        return redirect('home')


# def detail_post(request, pk, author):
   
#     post = Blog.objects.get(pk=pk)
#     if post.author.username == author:

#         context = {
#             'post':post
#         }
#         return render(request, 'post_details.html', context)
#     else:
#         return redirect('home')


def detail_post(request, pk, author):
    post = Blog.objects.get(pk=pk)
    if post.author.username == author:

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                data = comment_form.cleaned_data
                print(data['comment'])

                commentator = request.user
                new_comment = Comments(commentator=commentator, post=Blog.objects.get(pk=pk), comment=data['comment'])
                new_comment.save()

                comments = Comments.objects.filter(post=post)

                context = {
                    'post':post,
                    'comment_form': CommentForm(),
                    'comments': comments
                    }

                return render(request, 'post_details.html', context)

        else:
            comment_form = CommentForm()
            comments = Comments.objects.filter(post=post)
            context = {
                'post':post,
                'comment_form': comment_form,
                'comments':comments
            }
            
            return render(request, 'post_details.html', context)
    
    else:
        return redirect('home')




# Sección de posts

class PostSectionView(TemplateView):
    template_name = "post_section.html"


# Buscador de posteos

def post_search(request):
    search_form = PostSearch()
    if request.method == 'POST':
        search_form = PostSearch(request.POST)

        if search_form.is_valid():
            data = search_form.cleaned_data
            title_wanted = data['title']
            coincidences = Blog.objects.filter(title__icontains=title_wanted)
            search = True

            context = {
                'title_wanted':title_wanted,
                'coincidences':coincidences,
                'search':search,
                'search_form':search_form,
            }
            return render(request,'post_search.html',context)
        else:
            search_form = PostSearch()
            context = {
                'search_form':search_form
            }
            return render(request, 'post_search.html', context )

        
    else:
        search_form = PostSearch()
        coincidences = []
        search = False
        context = {
            'search_form':search_form,
            'coincidences':coincidences,
            'search':search
        }

        return render(request, 'post_search.html', context)


# Listado de todos los posteos

class PostListView(ListView):
    model = Blog
    template_name = 'post_list.html'


def my_post_list(request):
    author = request.user
    posts_list = Blog.objects.filter(author=author)

    context = {
        'posts_list':posts_list
    }

    return render(request, 'my_post_list.html', context)


# Comentarios

@login_required
def delete_comment(request, pk, pkcomment):
    comment = Comments.objects.get(pk=pkcomment)
    
    if comment.commentator == request.user or comment.post.author == request.user:
        if request.method == 'POST':
            confirmation = ConfirmationForm(request.POST)

            if confirmation.is_valid():
                data = confirmation.cleaned_data
                if data['confirmation']:
                    comment.delete()
                    next = request.POST.get('next', '/')
                    return redirect(next)
                
        else:
            confirmation = ConfirmationForm()
            print(comment)
            context = {
                'confirmation': confirmation,
                'comment':comment
            }

            return render(request,'delete_comment.html', context)

    else:
        return redirect('home')   


# @login_required
# def new_comment(request, pk):
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             data = comment_form.cleaned_data
#             commentator = request.user
#             new_comment = Blog(commentator=commentator, post=Blog.objects.get(pk=pk))
#             new_comment.save()
#             return redirect(request.path)    

#         else:
#             return render(request, 'create_comment.html', {'comment_form':comment_form, 'msj':'Datos con formato incorrecto'} )            
        
#     else:
#         comment_form = CommentForm()
#         context = {
#             'comment_form':comment_form,
#         }
#         return render(request,'create_comment.html',context)
