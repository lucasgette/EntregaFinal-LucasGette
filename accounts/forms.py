from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class CreateUser(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:'' for k in fields }



# Este modelo nos permite actualizar los datos del modelo User que vienen naturalmente

class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        help_texts = {k:'' for k in fields }

# Este modelo nos permitirá actualiza los datos del modelo que creamos para extender a User (bio y avatar)

class ProfileUpdateForm(forms.ModelForm):

    avatar = forms.ImageField(label='Avatar', widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)

    class Meta:
        model = UserProfile
        fields = ['description','website','avatar']



class SearchUser(forms.Form):
    usuario = forms.CharField(max_length=60, label='Nombre de usuario')





