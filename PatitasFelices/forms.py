from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Turno
import datetime

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FormTurnos(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['nombre', 'nombre_mascota', 'animal', 'edad_mascota', 'tipo', 'fecha', 'hora', 'contacto']
        labels = {
            'nombre': 'Nombre completo',
            'nombre_mascota': 'Nombre de la mascota',
            'animal': 'Tipo de Mascota',
            'edad_mascota': 'Edad de la mascota',
            'tipo': 'Tipo de turno',
            'fecha': 'Fecha del turno',
            'hora': 'Hora del turno',
            'contacto': 'Teléfono'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Fecha con fecha mínima y calendario
        self.fields['fecha'].widget = forms.DateInput(attrs={
            'type': 'date',
            'min': datetime.date.today().strftime('%Y-%m-%d')
        })

        # Validación de hora en intervalos de 30 minutos
        self.fields['hora'].widget = forms.Select(choices=[
            (f"{h}:{m:02d}", f"{h}:{m:02d}") for h in range(9, 21) for m in (0, 30)
        ])

        # Opciones del tipo de turno
        self.fields['tipo'].widget = forms.Select(choices=[
            ('veterinaria', 'Atención veterinaria'),
            ('cirugia', 'Cirugía'),
            ('imagenes', 'Imágenes'),
            ('peluqueria', 'Peluquería'),
        ])

        # Todos los campos requeridos
        for field in self.fields.values():
            field.required = True

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha.weekday() in (5, 6):  # 5 = sábado, 6 = domingo
            raise forms.ValidationError("No se dan turnos los fines de semana.")
        return fecha
