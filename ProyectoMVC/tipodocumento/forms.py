from django import forms
from .models import td, persona, ciudad

class tdForm(forms.ModelForm):

    class Meta:
         model = td

         fields = [
              'nombre',
              'descripcion'
         ]
         labels = {
              'nombre':'Nombre',
              'descripcion':'Descripción',
         }
         widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','required':''}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','required':''}),
        
         }

class CiudadForm(forms.ModelForm):
    class Meta:
        model = ciudad
        fields = ['nombre', 'descripcion']
        labels = {'nombre':'Nombre','descripcion':'Descripción'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','required':''}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','required':''}),
        
         }

class registroForm(forms.ModelForm):
     confirm_password = forms.CharField(widget=forms.PasswordInput())
     lugarResidencia=forms.ModelChoiceField(label="Lugar de Residencia",queryset=ciudad.objects.all(), empty_label="Seleccione una ciudad de residencia", widget=forms.Select(attrs={'class': 'form-control'}))
     tipodocumento= forms.ModelChoiceField(label="Tipo de Documento",queryset=td.objects.all(), empty_label="Seleccione un tipo de documento", widget=forms.Select(attrs={'class': 'form-control'}))
     class Meta:
          model = persona

          fields = [
               'nombres','apellidos','tipodocumento','documento',
               'lugarResidencia','fechanacimiento','email','telefono',
               'username','password'
               
          ]
          labels = {
               'nombres':'Nombres','apellidos':'Apellidos','documento':'Documento',
               'fechanacimiento':'Fecha de Nacimiento','email':'Email','telefono':'Teléfono',
               'username':'Usuario','password':'Contraseña'
          }
          widgets = {
               'nombres': forms.TextInput(attrs={'class':'form-control','required':''}),'apellidos'
               : forms.TextInput(attrs={'class':'form-control','required':''}),
               'documento': forms.TextInput(attrs={'class':'form-control','required':''}),'fechanacimiento': forms.DateInput(attrs={'class':'form-control','type':'date'}),
               'email': forms.TextInput(attrs={'class':'form-control','required':''}),'telefono': forms.TextInput(attrs={'class':'form-control','required':''}),
               'usuario': forms.TextInput(attrs={'class':'form-control','required':''}),
               'password': forms.PasswordInput(),
          }
          
          def clean(self):
               cleaned_data = super().clean()
               password = cleaned_data.get("password")
               confirm_password = cleaned_data.get("confirm_password")
               
               if password != confirm_password:
                    self.add_error('confirm_password', "Las contraseñas no coinciden.")
