from django import forms

class Formulario_Contacto(forms.Form):
    name = forms.CharField(max_length=200, 
                           required=True, 
                           label='Your name',
                           widget=forms.TextInput(attrs={'class': 'form-control text-center', 'placeholder': 'Tu nombre'}))
    
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control text-center', 'placeholder': 'Tu email'}))
    
    contenido = forms.CharField(label='conetenido',
                                widget=forms.Textarea(attrs={'class': 'form-control text-center','placeholder': 'escribe un comentario'}))
    
    
    
    
    
    
    