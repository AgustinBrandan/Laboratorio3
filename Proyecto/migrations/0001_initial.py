# Generated by Django 3.2.6 on 2022-10-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('materia', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'libro',
                'verbose_name_plural': 'libros',
            },
        ),
    ]
