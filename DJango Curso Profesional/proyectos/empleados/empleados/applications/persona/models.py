from django.db import models
from applications.departamento.models import Departamento

# Create your models here.
class Empleado(models.Model):
    """Modelo para tabla empleado"""
    
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    
    firt_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['last_name']
    
    def __str__(self):
        return str(self.id) + ' - ' + self.firt_name + ' - ' + self.last_name
