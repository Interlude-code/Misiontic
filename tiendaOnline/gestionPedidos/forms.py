from django import forms

class formularioContacto(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()
    