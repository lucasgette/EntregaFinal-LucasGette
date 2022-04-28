from django.shortcuts import render, redirect

from index.forms import ConfirmationForm
from .forms import CreateUser, UserUpdateForm, ProfileUpdateForm, SearchUser

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import UserProfile
from blogs.models import Blog


# Create your views here.


# INICIAR SESION - VIEW

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    # Si el usuario ya está loggeado, nos lleva a la Home page. En caso contrario, nos permite ir al formulario   

    else:
        if request.method == 'POST':
            login_form = AuthenticationForm(request, data=request.POST)
            # se almacena la información introducida por el usuario en el formulairo

            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                # Si la información en el formulario es valida, las almacena 
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('home')       

                else:
                    return render(request, 'login.html', {'login_form':login_form, 'msj':'El usuario no pudo ser autenticado. Por favor, reingresar los datos correctamente.'})     
            else:
                return render(request, 'login.html', {'login_form':login_form, 'msj':'Datos con formato incorrecto'} )
        else:
            login_form = AuthenticationForm()
            return render(request,'login.html', {'login_form':login_form} )


# CREAR USUARIO - VIEW

def register(request):
    if request.method == 'POST':
        register_form = CreateUser(request.POST)
        
        if register_form.is_valid():
            username = register_form.cleaned_data['username'] 
            #Esto es solo para sumarlo al contexto.
            register_form.save()
            return render(request,'index.html',{'registro_exitoso':f'Se creó el user {username}. Ya puedes iniciar sesion.'})
        else:
            return render(request, 'register.html',{'reg_form':register_form, 'msj':''})
    else:
        register_form = CreateUser()
        return render(request, 'register.html',{'reg_form':register_form})


# MODIFICAR USUARIO - VIEW

@login_required
def update_profile(request):
    if request.method== 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('my_profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
  
        usuario = request.user

        context = {
            'user_form':user_form,
            'profile_form':profile_form,
            'usuario': usuario
        }
        return render(request,'update_profile.html', context)


# BORRAR FOTO DE PERFIL - VIEW

@login_required
def delete_avatar(request):
    if request.user.userprofile.avatar == 'default.jpg':
        print('NOOOOOOOOOOOOO')
        return redirect('update_profile')

    else:
        if request.method == 'POST':
            confirmation = ConfirmationForm(request.POST)

            if confirmation.is_valid():
                data = confirmation.cleaned_data
                if data['confirmation']:
                    profile = UserProfile.objects.get(user=request.user)
                    profile.avatar.delete()
                    profile.avatar = 'default.jpg'
                    profile.save()
                    # perfil.avatar.delete()
                    # default.jpg
                    
           
                    
                return redirect('update_profile')
            
        else:
            confirmation = ConfirmationForm()

            context = {
                'confirmation': confirmation
            }

            return render(request,'delete_avatar.html', context)


# MI PERFIL


@login_required
def my_profile(request):
    user = request.user
     
    posts = Blog.objects.filter(author=user)

    context = {

        'usuario': user,
        'nombre': user.first_name,
        'apellido': user.last_name,
        'email': user.email,
        'avatar': user.userprofile.avatar,
        'description': user.userprofile.description,
        'website': user.userprofile.website,
        'date_joined': user.date_joined,
        'posts':posts

        }
    
    return render(request, 'my_profile.html', context)


# PERFIL DE OTROS USUARIOS

@login_required
def other_user_profile(request, username):
    if username == request.user.username:
        return redirect('my_profile')
    else:
        user = User.objects.get(username=username)

        posts = Blog.objects.filter(author=user)

        context = {

            'usuario': user,
            'nombre': user.first_name,
            'apellido': user.last_name,
            'avatar': user.userprofile.avatar,
            'description': user.userprofile.description,
            'website': user.userprofile.website,
            'date_joined': user.date_joined,
            'posts':posts

            }
        return render(request, 'other_user_profile.html', context)


# Buscador de usuarios

@login_required
def users_search(request):
    search_form = SearchUser()
    if request.method == 'POST':
        search_form = SearchUser(request.POST)

        if search_form.is_valid():
            data = search_form.cleaned_data
            users_wanted = data['usuario']
            coincidences = User.objects.filter(username__icontains=users_wanted)
            search = True

            contexto = {

                'users_wanted':users_wanted,
                'coincidences':coincidences,
                'search':search,
                'search_form':search_form,

            }
            return render(request,'search_user.html',contexto)
        else:
            return render(request, 'search_user.html', {} )

        
    else:
        all_users = User.objects.all()
        search_form = SearchUser()
        coincidences = []
        search = False
        contexto = {
            'search_form':search_form,
            'coincidences':coincidences,
            'search':search,
            'all_users' : all_users
        }

        return render(request, 'search_user.html', contexto)







