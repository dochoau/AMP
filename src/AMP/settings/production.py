from .base import *


SECRET_KEY = '_!u!p-o9emmom4r&!2!kmxij1*)264^hxthvjl%%vgwxa(l@#t'

# Debug de Desarrollo
DEBUG = True

# Host de la aplicación
ALLOWED_HOSTS = ['127.0.0.1']

# Archivos Estáticos
STATIC_URL = '/static/'

# base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
