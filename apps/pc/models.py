from django.db import models


# Create your models here.

class datos(models.Model):
	marca = models.CharField(blank=False, default='Generica', max_length=50)
	modelo = models.CharField(blank=True, max_length=50)
	capacidad = models.PositiveSmallIntegerField(blank=False)
	sufijos_capacidad = (
		('Mb','Mb'),
		('Gb','Gb'),
		('Tb','Tb')
		)
	unidad = models.CharField(blank=False, choices=sufijos_capacidad, default='Gb', max_length=2)
	serial = models.CharField(blank=True, max_length=50)

	def __str__(self):
		return ('%s - %s - %s%s') %(self.marca, self.modelo, self.capacidad,self.unidad)

	class Meta:
		abstract=True

class datos_basico(models.Model):	
	marca = models.CharField(blank=False, max_length=50)
	modelo = models.CharField(blank=False, max_length=50)
	serial = models.CharField(blank=True, max_length=50)
	capacidad = models.CharField(blank=True, max_length=50)

	def __str__(self):
		return ('%s - %s - %s') %(self.marca, self.modelo, self.capacidad)

	class Meta:
		abstract = True


class Ram(datos):
	def __str__(self):
		return ('%s - %s - %s%s') %(self.marca, self.modelo, self.capacidad,self.unidad)
	class Meta:
		verbose_name='Memoria Ram'
		verbose_name_plural='Memorias Ram'	

class DD(datos_basico):

	class Meta:
		verbose_name='Disco Duro'
		verbose_name_plural='Discos Duros'

class CdRom(datos_basico):
	class Meta:
		verbose_name='CD-ROM'

class Fuente(datos_basico):
	class Meta:
		verbose_name='Fuente de Poder'
		verbose_name_plural='Fuentes de Poder'

class Cpu(models.Model):
	fabricantes = (
		('INTEL', 'INTEL'),
		('AMD', 'AMD')
		)
	unidades = (
		('Mhz', 'Mhz'),
		('Ghz', 'Ghz')
		)
	fabricante = models.CharField(blank=False, choices=fabricantes, default='INTEL', max_length=50)
	modelo = models.CharField(blank=False, max_length=50)
	unidad = models.CharField(choices=unidades, default='Ghz', blank=False, max_length=50)
	capacidad = models.PositiveSmallIntegerField(blank=False)
	socket = models.CharField(blank=False, default='775', max_length=50)

	def __str__(self):
		return ('%s - %s - %s%s - %s') %(self.fabricante, self.modelo, self.capacidad, self.unidad, self.socket)

	class Meta:
		verbose_name='Procesador'
		verbose_name_plural='Procesadores'

class MoBo(datos_basico):

	class Meta:
		verbose_name='Tarjeta Madre'
		verbose_name_plural='Tarjetas Madre'

class Adicional(datos_basico):
	nombre = models.CharField(blank=False, max_length=50)

	class Meta:
		verbose_name="Dispositivo Adicional"
		verbose_name_plural='Dispositivos Adicionales'

class Estado_PC(models.Model):
	estado = models.CharField(blank=False, max_length=50)

	def __str__(self):
		return (self.estado)

class Desktop(models.Model):
	cliente = models.ForeignKey('cliente.Cliente')

	estado = models.ManyToManyField(Estado_PC)
	ram = models.ManyToManyField(Ram, verbose_name='Memorias Ram')
	dd = models.ManyToManyField(DD, verbose_name='Discos Duros')
	cdRom = models.ManyToManyField(CdRom, verbose_name='Quemadoras')
	adicional = models.ManyToManyField(Adicional, verbose_name='Dispositivos Adicionales', blank=True)

	fuente = models.ForeignKey(Fuente, verbose_name='Fuente de Poder')
	cpu = models.ForeignKey(Cpu, verbose_name='Procesador')
	moBo = models.ForeignKey(MoBo, verbose_name='Tarjeta Madre')
	detalles = models.TextField(default='Ninguna')

	def __str__(self):
		return('%s - %s') %(str(self.id), self.cliente)

	class Meta:
		verbose_name='Computadora'
		verbose_name_plural='Computadoras'

class Laptop(models.Model):
	cliente = models.ForeignKey('cliente.Cliente')

	estado = models.ManyToManyField(Estado_PC)
	marca = models.CharField(blank=False, max_length=50)
	modelo = models.CharField(blank=False, max_length=50)
	serial = models.CharField(blank=False, max_length=50)
	tipos=(
		('Mini','Mini'),
		('Laptop', 'Laptop')
		)
	tipo = models.CharField(choices=tipos, max_length=50)

	cargador = models.BooleanField(default=True)
	bateria = models.BooleanField(default= True)
	detalles = models.TextField(default='Ninguno')

	def __str__(self):
		return('%s - %s') %(str(self.id), self.cliente)

	class Meta:
		verbose_name='Laptop'
		verbose_name_plural='Laptops'