from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre
    
class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_mascota = models.CharField(max_length=100, null=True, blank=True)
    animal = models.CharField(max_length=100, null=True, blank=True)
    edad_mascota = models.CharField(max_length=100, null=True, blank=True)
    contacto = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    tipo = models.CharField(
        max_length=30,
        choices=[
            ('veterinaria', 'Atención veterinaria'),
            ('cirugia', 'Cirugía'),
            ('imagenes', 'Imágenes'),
            ('peluqueria', 'Peluquería'),
        ]
    )

    def __str__(self):
        return f"{self.nombre} - {self.nombre_mascosta} - {self.animal} - {self.edad_mascota} - {self.tipo} - {self.fecha} - {self.hora}"

