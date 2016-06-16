from django.db import models

# Create your models here.

class Cliente(models.Model):
	usuario = models.OneToOneField('main.Usuario', blank=True)
	nombre = models.CharField(blank=False, max_length=50)
	prefijos= (
		('0412','0412'),
		('0426','0426'),
		('0416','0416'),
		('0424','0424')
		)
	prefijo_telefono = models.CharField(blank=False, max_length=50, choices=prefijos)
	telefono = models.CharField(blank=False, max_length=7)
	ci = models.SmallIntegerField(blank=False)