from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Usuario, Tecnico, Servicio, Servicio_Tecnico_Desktop, Servicio_Tecnico_Laptop
from .forms import UserChangeForm, UserCreationForm

from .functions import generarPDF

# Register your models here.


@admin.register(Usuario)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(Group)

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    pass

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display=('nombre', 'precio')
    list_filter=('precio',)
    search_fields=('nombre',)
    

@admin.register(Servicio_Tecnico_Desktop)
class Servicio_TecnicoAdmin(admin.ModelAdmin):

    def getPDF(self, request, queryset):
        for servicio in queryset:
            return generarPDF('pdfservicio.html', servicio, servicio, 'Desktop')
    getPDF.short_description = "Generar PDF's"

    def button(self, obj):
        print(obj)
        link = u'<a class="button" href="/pdf/%s">PDF</a>' %(obj.id)
        return (link)
    button.short_description = 'PDF'
    button.allow_tags = True

    raw_id_fields=('cliente',)
    actions = ['getPDF']
    list_display = ['pc', 'tecnico', 'cliente', 'fecha_recepcion', 'fecha_finalizacion', 'fecha_entrega', 'button']

@admin.register(Servicio_Tecnico_Laptop)
class Servicio_TecnicoAdmin(admin.ModelAdmin):

    def getPDF(self, request, queryset):
        for servicio in queryset:
            return generarPDF('pdfservicio.html', servicio, servicio, 'Laptop')
    getPDF.short_description = "Generar PDF's"

    def button(self, obj):
        print(obj)
        link = u'<a class="button" href="/pdf/%s">PDF</a>' %(obj.id)
        return (link)
    button.short_description = 'PDF'
    button.allow_tags = True

    raw_id_fields=('cliente',)
    actions = ['getPDF']
    list_display = ['pc', 'tecnico', 'cliente', 'fecha_recepcion', 'fecha_finalizacion', 'fecha_entrega', 'button']