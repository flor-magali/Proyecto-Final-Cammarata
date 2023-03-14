
from django import forms
from AppPagweb.models import Usuario, Postear, Adoptame

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class PostearForm(forms.ModelForm):
    class Meta:
        model = Postear
        fields = '__all__'

class AdoptameForm(forms.ModelForm):
    class Meta:
        model = Adoptame
        fields = '__all__'