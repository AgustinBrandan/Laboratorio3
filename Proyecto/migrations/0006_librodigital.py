# Generated by Django 3.2.16 on 2022-12-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0005_libro_materia'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibroDigital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('materia', models.IntegerField()),
                ('autor', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'librodigital',
                'verbose_name_plural': 'librosdigitales',
            },
        ),
    ]
