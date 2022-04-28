
from django.urls import path
from .views import register, user_login, update_profile, delete_avatar, my_profile, other_user_profile, users_search

from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('accounts/register', register, name='register'),
    path('accounts/login', user_login, name='login'),
    path('accounts/logout', login_required(LogoutView.as_view(template_name='logout.html')), name='logout'),
    
    path('accounts/profile/my_profile', my_profile, name='my_profile'),
    path('accounts/profile/update', update_profile, name='update_profile'),
    path('accounts/profile/my_profile/change_password', PasswordChangeView.as_view(template_name='changepassword.html'),name='change_password'),
    path('accounts/profile/my_profile/password_changed', PasswordChangeDoneView.as_view(template_name='passwordsuccess.html'),name='password_change_done'),
       
    path('accounts/profile/update/delete-avatar', delete_avatar, name='delete_avatar'),

    path('accounts/profile/<str:username>', other_user_profile, name='other_user_profile'),
    path('accounts/search', users_search, name='users_search'),


]
