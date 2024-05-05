from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingresar constraseña',
        'class': 'form-control',
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar contraseña',
        'class': 'form-control',
    }))
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ingrese nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ingrese apellidos'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Ingrese número telefónico'
        self.fields['email'].widget.attrs['placeholder'] = 'Ingrese correo electrónico'
        
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'