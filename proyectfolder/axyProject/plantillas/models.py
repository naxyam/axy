from django.db import models
import datetime


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
    benef_grupoeta = models.ForeignKey('Grupoetareo', models.DO_NOTHING, db_column='benef_grupoeta')
    benef_huerfano = models.IntegerField()
    benef_nav = models.IntegerField()
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
    

    class Meta:
        managed = True
        db_table = 'beneficiario'
        verbose_name = 'Beneficiario'
        verbose_name_plural ='Beneficiarios'

    def __str__(self):
        return self.benef_apellidos + self.benef_nombres
    
    def calc_edad(self):
        year = now = datetime.datetime.now().year
        return year - self.benef_fechanac


class Hobbies(models.Model):
    hob_id = models.AutoField(primary_key=True)
    hob_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'hobbies'
        verbose_name = 'Hobbie'
        verbose_name_plural ='Hobbies'

    def __str__(self):
        return self.hob_nombre 


class Hobbiesxbenef(models.Model):
    hobxben_id = models.IntegerField(primary_key=True)
    hobxben_idben = models.ForeignKey(Beneficiario, models.DO_NOTHING, db_column='hobxben_idben', blank=True, null=True)
    hobxben_idhob = models.ForeignKey(Hobbies, models.DO_NOTHING, db_column='hobxben_idhob', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hobbiesxbenef'
        verbose_name = 'HobbiexBenef'
        verbose_name_plural ='HobbiesxBenef'

    


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


class Materiasxbenef(models.Model):
    matxben_id = models.IntegerField(primary_key=True)
    matxben_idben = models.ForeignKey(Beneficiario, models.DO_NOTHING, db_column='matxben_idben', blank=True, null=True)
    matxben_idmat = models.ForeignKey(Materias, models.DO_NOTHING, db_column='matxben_idmat', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'materiasxbenef'
        verbose_name = 'MateriaxBenef'
        verbose_name_plural ='MateriasxBenef'

    

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


class Deberesxbenef(models.Model):
    debxben_id = models.IntegerField(primary_key=True)
    debxben_idben = models.ForeignKey(Beneficiario, models.DO_NOTHING, db_column='debxben_idben', blank=True, null=True)
    debxben_iddeb = models.ForeignKey(Deberes, models.DO_NOTHING, db_column='debxben_iddeb', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'deberesxbenef'
        verbose_name = 'DeberxBenef'
        verbose_name_plural ='DeberesxBenef'

    