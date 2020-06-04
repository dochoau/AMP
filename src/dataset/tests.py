from django.test import TestCase
from .models import DataSet
from core.models import User

# probar la creación del slug


class DataSetTestCase(TestCase):
    def setUp(self):
        """Esta función ejecuta una acción antes de ejecutar las pruebas"""
        User.objects.create(username="admin")
        user = User.objects.get(pk=1)
        DataSet.objects.create(nombre="data set 1 super",
                               descripcion="descripcion", creador=user)

    def test_check_slugs(self):
        object_1 = DataSet.objects.get(pk=1)
        self.assertEquals(object_1.slug, "data-set-1-super")
