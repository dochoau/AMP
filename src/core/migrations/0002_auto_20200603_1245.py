# Generated by Django 2.1.1 on 2020-06-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nit_empresa',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombre_empresa',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel_contacto',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
