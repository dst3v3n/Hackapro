# Generated by Django 5.1 on 2024-08-25 05:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('powerbi', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nucleo_familiar', models.CharField(choices=[('Pareja sin hijos dependientes', 'Pareja sin hijos dependientes'), ('Familia monoparental con hijos dependientes', 'Familia monoparental con hijos dependientes'), ('Hogar grupal', 'Hogar grupal'), ('Persona soltera', 'Persona soltera'), ('Pareja con hijos dependientes', 'Pareja con hijos dependientes'), ('Hogar multifamiliar', 'Hogar multifamiliar'), ('', 'selecciona tu nucleo familiar'), ('Otro hogar unifamiliar', 'Otro hogar unifamiliar')], default='', max_length=50)),
                ('cambios_trabajo', models.CharField(choices=[('Ni poco probable ni probable', 'Ni poco probable ni probable'), ('Muy probable', 'Muy probable'), ('Algo improbable', 'Algo improbable'), ('', 'selecciona tu respuesta'), ('Muy improbable', 'Muy improbable'), ('Algo probable', 'Algo probable')], default='Muy probable', max_length=40)),
                ('tiempoDesplazamiento', models.DecimalField(decimal_places=1, max_digits=10)),
                ('horasDomestica', models.DecimalField(decimal_places=1, max_digits=10)),
                ('horasPersonal', models.DecimalField(decimal_places=1, max_digits=10)),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
                'db_table': 'perfiles',
                'ordering': ['myuser', '-myuser'],
            },
        ),
        migrations.CreateModel(
            name='powerbi_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='powerbi.categorias')),
                ('myuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'powerbi_user',
                'verbose_name_plural': 'powerbi_user',
                'db_table': 'powerbi_user',
                'ordering': ['myuser', '-myuser'],
            },
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempoDedicado', models.DecimalField(decimal_places=1, max_digits=10)),
                ('position', models.CharField(choices=[('Profesionales, científicos y técnicos', 'Profesionales, científicos y técnicos'), ('Transporte, postal y almacenamiento', 'Transporte, postal y almacenamiento'), ('Manufactura', 'Manufactura'), ('Comercio mayorista', 'Comercio mayorista'), ('Minería', 'Minería'), ('Educación y formación', 'Educación y formación'), ('Alojamiento y alimentos', 'Alojamiento y alimentos'), ('Administración y apoyo', 'Administración y apoyo'), ('Salud', 'Salud'), ('Atención de la salud y asistencia social', 'Atención de la salud y asistencia social'), ('Medios de información y telecomunicaciones', 'Medios de información y telecomunicaciones'), ('Otros servicios', 'Otros servicios'), ('Artes y recreación', 'Artes y recreación'), ('Agricultura, silvicultura y pesca', 'Agricultura, silvicultura y pesca'), ('Finanzas y seguros', 'Finanzas y seguros'), ('Alquiler, arrendamiento y bienes raíces', 'Alquiler, arrendamiento y bienes raíces'), ('Comercio minorista', 'Comercio minorista'), ('Administración pública y seguridad', 'Administración pública y seguridad'), ('Construcción', 'Construcción'), ('', 'Selecciona su sector'), ('Electricidad, gas, agua y desechos', 'Electricidad, gas, agua y desechos')], default='', max_length=105, null=True)),
                ('sector', models.CharField(choices=[('Gerentes - Gerentes de hostelería, retail y servicios', 'Gerentes - Gerentes de hostelería, retail y servicios'), ('Obreros - Trabajadores de granjas, silvicultura y jardines', 'Obreros - Trabajadores de granjas, silvicultura y jardines'), ('Trabajadores de servicios comunitarios y personales - Trabajadores de hostelería', 'Trabajadores de servicios comunitarios y personales - Trabajadores de hostelería'), ('Profesionales - Profesionales en derecho, social y bienestar', 'Profesionales - Profesionales en derecho, social y bienestar'), ('Operadores de maquinaria y conductores - Almacenistas', 'Operadores de maquinaria y conductores - Almacenistas'), ('Técnicos y trabajadores calificados - Trabajadores calificados en automoción e ingeniería', 'Técnicos y trabajadores calificados - Trabajadores calificados en automoción e ingeniería'), ('Profesionales - Profesionales de la salud', 'Profesionales - Profesionales de la salud'), ('Gerentes - Directores ejecutivos, gerentes generales y legisladores', 'Gerentes - Directores ejecutivos, gerentes generales y legisladores'), ('Trabajadores de ventas - Representantes y agentes de ventas', 'Trabajadores de ventas - Representantes y agentes de ventas'), ('Gerentes - Gerentes especializados', 'Gerentes - Gerentes especializados'), ('Profesionales - Profesionales en diseño, ingeniería, ciencia y transporte', 'Profesionales - Profesionales en diseño, ingeniería, ciencia y transporte'), ('Técnicos y trabajadores calificados - Trabajadores calificados en electrotecnología y telecomunicaciones', 'Técnicos y trabajadores calificados - Trabajadores calificados en electrotecnología y telecomunicaciones'), ('Trabajadores de servicios comunitarios y personales - Trabajadores de apoyo en salud y bienestar', 'Trabajadores de servicios comunitarios y personales - Trabajadores de apoyo en salud y bienestar'), ('Técnicos y trabajadores calificados - Técnicos en ingeniería, TIC y ciencia', 'Técnicos y trabajadores calificados - Técnicos en ingeniería, TIC y ciencia'), ('Obreros - Obreros de construcción y minería', 'Obreros - Obreros de construcción y minería'), ('Trabajadores de ventas - Apoyo a las ventas', 'Trabajadores de ventas - Apoyo a las ventas'), ('Obreros - Asistentes de preparación de alimentos', 'Obreros - Asistentes de preparación de alimentos'), ('Trabajadores de oficina y administrativos - Otros trabajadores clericales y administrativos', 'Trabajadores de oficina y administrativos - Otros trabajadores clericales y administrativos'), ('Técnicos y trabajadores calificados - Trabajadores calificados en animales y horticultura', 'Técnicos y trabajadores calificados - Trabajadores calificados en animales y horticultura'), ('Gerentes - Agricultores y gerentes de granjas', 'Gerentes - Agricultores y gerentes de granjas'), ('Trabajadores de ventas - Asistentes de ventas y vendedores', 'Trabajadores de ventas - Asistentes de ventas y vendedores'), ('Técnicos y trabajadores calificados - Trabajadores calificados en alimentos', 'Técnicos y trabajadores calificados - Trabajadores calificados en alimentos'), ('Trabajadores de oficina y administrativos - Asistentes personales y secretarias', 'Trabajadores de oficina y administrativos - Asistentes personales y secretarias'), ('Técnicos y trabajadores calificados - Trabajadores calificados en construcción', 'Técnicos y trabajadores calificados - Trabajadores calificados en construcción'), ('Trabajadores de oficina y administrativos - Apoyo clerical y de oficina', 'Trabajadores de oficina y administrativos - Apoyo clerical y de oficina'), ('Trabajadores de oficina y administrativos - Gerentes de oficina y administradores de programas', 'Trabajadores de oficina y administrativos - Gerentes de oficina y administradores de programas'), ('Obreros - Otros obreros', 'Obreros - Otros obreros'), ('Obreros - Limpiadores y trabajadores de lavandería', 'Obreros - Limpiadores y trabajadores de lavandería'), ('Operadores de maquinaria y conductores - Operadores de plantas móviles', 'Operadores de maquinaria y conductores - Operadores de plantas móviles'), ('Obreros - Trabajadores de procesos en fábricas', 'Obreros - Trabajadores de procesos en fábricas'), ('Técnicos y trabajadores calificados - Otros técnicos y trabajadores calificados', 'Técnicos y trabajadores calificados - Otros técnicos y trabajadores calificados'), ('', 'Selecciona su cargo'), ('Profesionales - Profesionales de las artes y los medios', 'Profesionales - Profesionales de las artes y los medios'), ('Profesionales - Profesionales de TIC', 'Profesionales - Profesionales de TIC'), ('Trabajadores de servicios comunitarios y personales - Cuidadores y asistentes', 'Trabajadores de servicios comunitarios y personales - Cuidadores y asistentes'), ('Trabajadores de oficina y administrativos - Trabajadores clericales generales', 'Trabajadores de oficina y administrativos - Trabajadores clericales generales'), ('Profesionales - Profesionales en educación', 'Profesionales - Profesionales en educación'), ('Operadores de maquinaria y conductores - Conductores de carretera y ferrocarril', 'Operadores de maquinaria y conductores - Conductores de carretera y ferrocarril'), ('Trabajadores de servicios comunitarios y personales - Trabajadores de servicios de protección', 'Trabajadores de servicios comunitarios y personales - Trabajadores de servicios de protección'), ('Operadores de maquinaria y conductores - Operadores de máquinas y plantas estacionarias', 'Operadores de maquinaria y conductores - Operadores de máquinas y plantas estacionarias'), ('Profesionales - Profesionales en negocios, recursos humanos y mercadeo', 'Profesionales - Profesionales en negocios, recursos humanos y mercadeo'), ('Trabajadores de oficina y administrativos - Oficinistas de consulta y recepcionistas', 'Trabajadores de oficina y administrativos - Oficinistas de consulta y recepcionistas'), ('Trabajadores de oficina y administrativos - Oficinistas numéricos', 'Trabajadores de oficina y administrativos - Oficinistas numéricos')], default='', max_length=105, null=True)),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'trabajo',
                'verbose_name_plural': 'trabajos',
                'db_table': 'trabajos',
                'ordering': ['myuser', '-myuser'],
            },
        ),
    ]
