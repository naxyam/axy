from django.db import models
import datetime

from django.db.models.enums import Choices, ChoicesMeta
from django.utils.regex_helper import Choice


class Religion(models.Model):
    rel_id = models.AutoField(primary_key=True)
    rel_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'religion'
        verbose_name = 'Religion'
        verbose_name_plural ='Religiones'

    def __str__(self):
        return self.rel_nombre


class Sexo(models.Model):
    sex_id = models.AutoField(primary_key=True)
    sex_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'sexo'
        verbose_name = 'Sexo'
        verbose_name_plural ='Sexos'

    def __str__(self):
        return self.sex_nombre


class Rendimientoacademico(models.Model):
    rendiaca_id = models.AutoField(primary_key=True)
    rendiaca_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'rendimientoacademico'
        verbose_name = 'Rendimiento Academico'
        verbose_name_plural ='Rendimientos Academicos'

    def __str__(self):
        return self.rendiaca_nombre

class Educacionformal(models.Model):
    eformal_id = models.IntegerField(primary_key=True)
    eformal_nombre = models.CharField(max_length=100)
    eformal_descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'educacionformal'
        verbose_name = 'Educación Formal'
        verbose_name_plural = 'Educación Formal'

    def __str__(self):
        return self.eformal_nombre


class Grupoetareo(models.Model):
    grupeta_id = models.IntegerField(primary_key=True)
    grupeta_nombre = models.CharField(max_length=100)
    grupeta_descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'grupoetareo'
        verbose_name = 'GrupoEtareo'
        verbose_name_plural ='GruposEtareos'

    def __str__(self):
        return self.grupeta_nombre



class Actividadescristianas(models.Model):
    activcris_id = models.AutoField(primary_key=True)
    activcris_nombre = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'actividadescristianas'
        verbose_name = 'Actividades Cristianas'
        verbose_name_plural ='Actividades Cristianas'

    def __str__(self):
        return self.activcris_nombre

class Ciudades(models.Model):
    ciu_id = models.AutoField(primary_key=True)
    ciu_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'ciudades'
        verbose_name = 'Ciudad'
        verbose_name_plural ='Ciudades'

    def __str__(self):
        return self.ciu_nombre


class Departamento(models.Model):
    dep_id = models.AutoField(primary_key=True)
    dep_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'departamento'
        verbose_name = 'Departamento'
        verbose_name_plural ='Departamentos'

    def __str__(self):
        return self.dep_nombre

class Beneficiario(models.Model):
    benef_id = models.CharField(primary_key=True, max_length=20)
    benef_nombres = models.CharField(max_length=200)
    benef_apellidos = models.CharField(max_length=200)
    benef_nombrepref = models.CharField(max_length=200)
    benef_sexo = models.ForeignKey('Sexo', models.DO_NOTHING, db_column='benef_sexo')
    benef_fechanac = models.DateField()
    benef_edad = models.PositiveIntegerField('Edad', db_column='benef_edad')
    benef_grupoeta = models.ForeignKey('Grupoetareo', models.DO_NOTHING, db_column='benef_grupoeta')
    benef_huerfano = models.BooleanField()
    benef_nav = models.BooleanField()
    benef_barrio = models.CharField(max_length=200, blank=True, null=True)
    benef_direccion = models.CharField(max_length=200)
    benef_telefono = models.BigIntegerField(blank=True, null=True)
    benef_correo = models.CharField(max_length=120)
    benef_ciudad = models.ForeignKey('Ciudades', models.DO_NOTHING, db_column='benef_ciudad')
    benef_departamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='benef_departamento')
    benef_eduformal = models.ForeignKey('Educacionformal', models.DO_NOTHING, db_column='benef_eduformal')
    benef_rendiaca = models.ForeignKey('Rendimientoacademico', models.DO_NOTHING, db_column='benef_rendiaca')
    benef_religion = models.ForeignKey('Religion', models.DO_NOTHING, db_column='benef_religion')
    benef_activcrist = models.ForeignKey('Actividadescristianas', models.DO_NOTHING, db_column='benef_activcrist')
    benef_img = models.ImageField(upload_to='plantillas', default= 'null')
    benef_created = models.DateTimeField(auto_now_add=True)
    benef_updated = models.DateTimeField(auto_now_add=True)
    benef_hobbies = models.ManyToManyField('Hobbies')
    benef_materias = models.ManyToManyField('Materias')
    benef_deberes = models.ManyToManyField('Deberes')
    

    class Meta:
        managed = True
        db_table = 'beneficiario'
        verbose_name = 'Beneficiario'
        verbose_name_plural ='Beneficiarios'

    def __str__(self):
        return self.benef_id + ' ' + self.benef_apellidos + ' ' + self.benef_nombres
    
    def calc_edad(self):
        year = now = datetime.datetime.now().year
        return year - self.benef_fechanac.year


class Hobbies(models.Model):
    hob_id = models.AutoField(primary_key=True)
    hob_nombre = models.CharField(max_length=50,)

    class Meta:
        managed = True
        db_table = 'hobbies'
        verbose_name = 'Hobbie'
        verbose_name_plural ='Hobbies'

    def __str__(self):
        return self.hob_nombre 


class Materias(models.Model):
    mat_id = models.AutoField(primary_key=True)
    mat_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'materias'
        verbose_name = 'Materia'
        verbose_name_plural ='Materias'

    def __str__(self):
        return self.mat_nombre


   
class Deberes(models.Model):
    deb_id = models.AutoField(primary_key=True)
    deb_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'deberes'
        verbose_name = 'Deber'
        verbose_name_plural ='Deberes'

    def __str__(self):
        return self.deb_nombre

class Historiaclinica(models.Model):
    histclinica_beneid = models.ForeignKey(Beneficiario, models.DO_NOTHING, db_column='histclinica_beneid', blank=True, null=True)
    histclinica_peso = models.FloatField(blank=True, null=True)
    histclinica_talla = models.FloatField(blank=True, null=True)
    histclinica_tratmedico = models.TextField(db_column='histclinica_tratMedico', blank=True, null=True)  
    histclinica_disfisica = models.ManyToManyField('Discapacidadesfisicas')
    histclinica_dismental = models.ManyToManyField('Discapacidadesmentales')
    histclinica_enfcronica = models.ManyToManyField('Enfermedadcronica')
    histclinica_created = models.DateTimeField(auto_now_add=True)
    histclinica_updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'historiaclinica'
        verbose_name = 'Historia Clínica'
        verbose_name_plural ='Historias Clínicas'

    def __str__(self):
        return self.id


class Discapacidadesfisicas(models.Model):
    disfisica_nombre = models.CharField(max_length=100)
    disfisica_descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'discapacidadesfisicas'
        verbose_name = 'Discapacidad física'
        verbose_name_plural ='Discapacidades físicas'
    def __str__(self):
        return self.disfisica_nombre


class Discapacidadesmentales(models.Model):
    dismental_nombre = models.CharField(max_length=100)
    dismental_descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'discapacidadesmentales'
        verbose_name = 'Discapacidad mental'
        verbose_name_plural ='Discapacidades mentales'
    
    def __str__(self):
        return self.dismental_nombre


class Enfermedadcronica(models.Model):
    enfcronica_nombre = models.CharField(max_length=100)
    enfcronica_descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'enfermedadcronica'
        verbose_name = 'Enfermedad crónica'
        verbose_name_plural ='Enfermedades crónicas'

    def __str__(self):
        return self.enfcronica_nombre




    