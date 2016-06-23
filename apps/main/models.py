#encoding:utf-8
from django.db import models

#imports necesarios para crear un Custom User Manager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


#Clase que hereda las funcionalidades y metodo necesario para la creacion de usuarios
class UserManager(BaseUserManager, models.Manager):

	#La siguiente funcion se encarga de crear el usuario en la base de datos, de acuerdo a los parametros recibidos
	def _create_user(self, username, email, password, is_staff,
				is_superuser, **extra_fields):

		#se normaliza y comprueba que se reciba un correro electronico
		email = self.normalize_email(email)
		if not email:
			raise ValueError('El email debe ser obligatorio')

		#Se crea un objeto con los datos recibidos por parametro
		user = self.model(username = username, email=email, is_active=True,
				is_staff = is_staff, is_superuser = is_superuser, **extra_fields)

		#Se realiza el proceso de hash del password o contraseña
		user.set_password(password)

		#Se garda el usuario en la base de datos utilizada actualmente
		user.save( using = self._db)

		#Se retorna el usuario creado
		return user

	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False,
				False, **extra_fields)

	def create_superuser(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, True,
				True, **extra_fields)

#Modelo Usuario, utilizado por el modelo Cliente, el modelo comercio.
#Tambien utilizado como Administrador o superusuario.
class Usuario(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(max_length=100, unique=True)
	email = models.EmailField(unique=True)

	#Se especifica el Manager para el modelo de usuario
	objects = UserManager()

	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)

	#Se especifica el campo a utilizar como Nombre de Usuario
	USERNAME_FIELD = 'username'
	#Se especifican los campos requeridos.
	REQUIRED_FIELDS = ['email']

	#Funcion que retorna el nombre de usuario, como nombre corto del objeto, al realizarse un llamado a este.
	def get_short_name(self):
		return self.username

class Tecnico(models.Model):
	usuario = models.OneToOneField(Usuario, blank=True)
	nombre = models.CharField(blank=False, max_length=50)
	prefijos= (
		('0412','0412'),
		('0426','0426'),
		('0416','0416'),
		('0424','0424')
		)
	prefijo_telefono = models.CharField(blank=False, max_length=50, choices=prefijos)
	telefono = models.CharField(blank=False, max_length=7)

	def __str__(self):
		return (self.nombre)


class Servicio(models.Model):
	nombre = models.CharField(blank=False, max_length=50)
	precio = models.PositiveSmallIntegerField(blank=False)

	def __str__(self):
		return(self.nombre + ' ' + str(self.precio))

	class Meta:
		verbose_name='Servicio'
		verbose_name_plural='Servicios'

class Servicio_Tecnico(models.Model):
	cliente = models.ForeignKey('cliente.Cliente')
	tecnico = models.ForeignKey(Tecnico)
	pc = models.ForeignKey('pc.Desktop')
	#laptop = models.ForeignKey('pc.Laptop')

	servicios = models.ManyToManyField(Servicio)

	total = models.PositiveSmallIntegerField(blank=True)
	abono = models.PositiveSmallIntegerField(blank=True)
	cancelado = models.BooleanField(blank=False)
	fecha_recepcion = models.DateField(auto_now_add=True)
	fecha_finalizacion = models.DateField(blank=True)
	fecha_entrega = models.DateField(blank=True)
	observaciones = models.TextField(blank=False, default='Ninguna')

	class Meta:
		verbose_name='Servicio Tecnico'
		verbose_name_plural='Servicios Tecnicos'
