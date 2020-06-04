from django.db import models
from django.conf import settings
from AMP.utils import unique_slug_generator
from django.db.models.signals import pre_save


class DataSet(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    creador = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    metadata = models.FileField(upload_to="version/%Y/%M/%D/", null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre


# Con esta función y la línea de abajo creo el slug para el DataSet
def data_set_slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, title=instance.nombre)


pre_save.connect(data_set_slug_save, sender=DataSet)


class DataSetFileVersion(models.Model):
    data_set = models.ForeignKey(
        DataSet, on_delete=models.CASCADE)
    num_version = models.AutoField(primary_key=True)
    fecha = models.DateField()
    extension_documento = models.CharField(max_length=8)
    documento = models.FileField(upload_to="version/%Y/%M/%D/")

    def __str__(self):
        return f"{self.data_set}/V/{self.num_version}"


class DataSetApi(models.Model):
    data_set = models.ForeignKey(
        DataSet, on_delete=models.CASCADE)
    num_version = models.IntegerField()
    api_name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return f"{self.data_set}/V/{self.num_version}"


class DataSetFileLibrary (models.Model):
    data_set_files = models.ManyToManyField('DataSetFileVersion', blank=True)
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_adquirencia = models.DateField(auto_now_add=True)


class DataSetApiLibrary (models.Model):
    data_set_api = models.ManyToManyField('DataSetApi', blank=True)
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_adquirencia = models.DateField(auto_now_add=True)
