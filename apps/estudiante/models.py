from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Estudiante(models.Model):
	# cedula
	# apellidos
	# nombres
	# estado ciudad pais
	#email
	#celular
    id_estudiante = models.AutoField(primary_key=True)
    cedula = models.CharField(
        max_length=15, null=False, blank=False, unique=True, verbose_name=_('Nombres del Estudiante'))
    nombres = models.CharField(
        max_length=100, null=False, blank=False, default='', verbose_name=_('Nombres del Estudiante'))
    apellidos = models.CharField(
        max_length=100, null=False, blank=False, default='', verbose_name=_('Nombres del Estudiante'))
    fecha_nac = models.DateField(
        auto_now_add=False, null=True, blank=True, editable=True, verbose_name=_('Fecha de Nacimiento'))
    celular = models.CharField(
        max_length=20, null=False, blank=False, default='', verbose_name=_('Observaciones'))
    correo_electronico = models.EmailField( max_length=250, null=False, blank=False, default='',
        verbose_name=_('correo electrónico'))

    class Meta:
        db_table = 'estudiantes'
        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'

    def __str__(self):
        return 'Estudiante #{}'.format(self.id_estudiante)