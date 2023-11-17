from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=250, blank=False, null=False)
    estado = models.BooleanField('Activo/No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural='Categorías'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del autor', max_length=100,blank=False,null=False)
    apellido = models.CharField('Apellido del autor', max_length=100,blank=False,null=False)
    estado = models.BooleanField('Activo/No Activo', default=True)
    instagram = models.URLField(
        'Instagram', 
                            max_length=300, 
                            blank=True,)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion = models.CharField('Descripción', max_length=110, blank=False, null=False)
    contenido = RichTextField('Contenido', null=False)
    imagen = models.URLField(max_length=255, blank=False, null=False)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Activo/No Activo', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.titulo


 