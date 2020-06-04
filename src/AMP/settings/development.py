from .base import *


SECRET_KEY = '_!u!p-o9emmom4r&!2!kmxij1*)264^hxthvjl%%vgwxa(l@#t'

# Debug de Desarrollo
DEBUG = True

# Host de la aplicación
ALLOWED_HOSTS = ['127.0.0.1']

# Archivos Estáticos
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
