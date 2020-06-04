from django.contrib import admin
from .models import DataSet, DataSetApi, DataSetFileVersion, DataSetFileLibrary, DataSetApiLibrary

# Register your models here.

admin.site.register(DataSet)
admin.site.register(DataSetFileVersion)
admin.site.register(DataSetApi)
admin.site.register(DataSetFileLibrary)
admin.site.register(DataSetApiLibrary)
