from django.contrib import admin

from .models import Desktop, Ram, DD, CdRom, MoBo, Fuente, Cpu, Adicional, Laptop, Estado_PC
# Register your models here.

@admin.register(Desktop)
class DesktopAdmin(admin.ModelAdmin):
	pass

@admin.register(Ram)
class RamAdmin(admin.ModelAdmin):
	pass

@admin.register(DD)
class DDAdmin(admin.ModelAdmin):
	pass

@admin.register(CdRom)
class CdRomAdmin(admin.ModelAdmin):
	pass

@admin.register(MoBo)
class MoBoAdmin(admin.ModelAdmin):
	pass

@admin.register(Fuente)
class FuenteAdmin(admin.ModelAdmin):
	pass

@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
	pass

@admin.register(Adicional)
class AdicionalAdmin(admin.ModelAdmin):
	pass

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
	pass

@admin.register(Estado_PC)
class EstadoPCADmin(admin.ModelAdmin):
	pass