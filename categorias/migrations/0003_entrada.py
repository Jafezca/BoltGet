# Generated by Django 3.2.4 on 2021-12-07 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_alter_categoria_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('descripcion', models.CharField(max_length=800)),
                ('enlace', models.URLField()),
                ('version', models.IntegerField()),
                ('nombre_archivo', models.CharField(max_length=256)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('publicado', models.BooleanField()),
            ],
        ),
    ]
