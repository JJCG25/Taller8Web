from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class td(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length = 30)
    descripcion= models.CharField(max_length = 500) 
    
    def __str__(self):
        return self.nombre

class ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length = 30)
    descripcion= models.CharField(max_length = 500)    

    def __str__(self):
        return self.nombre

class PersonaManager(BaseUserManager):
    def create_user(self, usuario, password=None, **extra_fields):
        if not usuario:
            raise ValueError('El campo Usuario es obligatorio.')
        user = self.model(usuario=usuario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(usuario, password, **extra_fields)

class persona(AbstractBaseUser):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    idtipodocumento = models.ForeignKey(td, on_delete=models.CASCADE)
    documento = models.BigIntegerField()
    idciudad = models.ForeignKey(ciudad, on_delete=models.CASCADE)
    fechanacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.BigIntegerField()
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = PersonaManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombres', 'apellidos', 'idtipodocumento', 'documento', 'idciudad', 'fechanacimiento', 'email', 'telefono']

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

# Create your models here.
