
import imp
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import delete_comment, new_post, detail_post, edit_post, delete_post, post_search, PostSectionView, PostListView, my_post_list, delete_comment

urlpatterns = [
    #Seeción principal de posts
    path('post-section/', PostSectionView.as_view(), name='post_section'),
    path('post/search', post_search, name='post_search'),
        # Listado total
    path('pages',PostListView.as_view(), name='post_list'),
        # Listado propio
    path('my-pages', my_post_list , name='my_post_list'),
    # CRUD para posts
    path('new-post', new_post , name='new_post'),
    path('pages/<int:pk>/edit', edit_post, name='edit_post'),
    path('pages/<int:pk>/delete', delete_post, name='delete_post'),
    path('pages/<str:author>/<int:pk>', detail_post, name='post_detail'),
    # Comentarios
    path('pages/<int:pk>/delete-comments/<int:pkcomment>', delete_comment, name='delete_comment')






    



]
