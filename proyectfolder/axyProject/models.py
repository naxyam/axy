# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models






class Cargos(models.Model):
    car_id = models.IntegerField(primary_key=True)
    car_nombre = models.CharField(max_length=50)
    car_desc = models.CharField(max_length=50)
    esta = models.ForeignKey('Estados', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'cargos'









class Entregaregalo(models.Model):
    entregalo_id = models.IntegerField(primary_key=True)
    benef_id_field = models.IntegerField(db_column='benef_id_')  # Field renamed because it ended with '_'.
    entregalo_fecha = models.DateField()
    entregalo_ingreso = models.FloatField()
    entregalo_entregado = models.IntegerField()
    entregalo_responsable = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'entregaregalo'


class Entregaregalos(models.Model):
    entrerega_id = models.IntegerField(primary_key=True)
    plant = models.ForeignKey('Plantilla', models.DO_NOTHING)
    entregalo_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'entregaregalos'


class Estadocivil(models.Model):
    estcivil_id = models.IntegerField(primary_key=True)
    estcivil_descr = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'estadocivil'


class Estados(models.Model):
    esta_id = models.IntegerField(primary_key=True)
    esta_nombre = models.CharField(max_length=50)
    esta_descripcion = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'estados'


class Fonollamada(models.Model):
    fllamada_id = models.DateField()
    plant = models.ForeignKey('Plantilla', models.DO_NOTHING)
    infllamada = models.OneToOneField('Infollamada', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = True
        db_table = 'fonollamada'


class Fsregistro(models.Model):
    fsregistro_id = models.IntegerField(primary_key=True)
    plant = models.ForeignKey('Plantilla', models.DO_NOTHING)
    bebef_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'fsregistro'



class Hogares(models.Model):
    hog_id = models.CharField(primary_key=True, max_length=50)
    benf_id = models.IntegerField()
    hog_padconv = models.IntegerField()
    hog_padrevivo = models.IntegerField()
    hog_padconvnino = models.IntegerField()
    sitlaboralpadre = models.ForeignKey('Situacionlaboralpadre', models.DO_NOTHING)
    estcivil = models.ForeignKey(Estadocivil, models.DO_NOTHING)
    hog_madrevivenino = models.IntegerField()
    hog_madreviva = models.IntegerField()
    sitlaboralmadre_id = models.IntegerField()
    ocupadre = models.ForeignKey('Ocupacionpadre', models.DO_NOTHING, db_column='Ocupadre_id')  # Field name made lowercase.
    ocumadre = models.ForeignKey('Ocupacionmadre', models.DO_NOTHING)
    ingre = models.ForeignKey('Rangoingresos', models.DO_NOTHING)
    hog_cont_viviendo = models.IntegerField()
    hog_porque = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'hogares'


class Infollamada(models.Model):
    infllamada_id = models.IntegerField(primary_key=True)
    benef = models.ForeignKey(Beneficiario, models.DO_NOTHING)
    infllamada_numtelef = models.CharField(max_length=20)
    infllamada_fecha = models.DateTimeField()
    infllamada_razon = models.TextField()
    infllamada_compromiso = models.TextField()
    infllamada_durallam = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'infollamada'


class Informacionvisita(models.Model):
    infovisi_id = models.IntegerField(primary_key=True)
    benef_id = models.CharField(max_length=50)
    infovisi_famcrist = models.IntegerField()
    infovisi_fecha = models.DateField()
    infovisi_proposito = models.CharField(max_length=200)
    hogar = models.ForeignKey(Hogares, models.DO_NOTHING)
    integrante_id = models.IntegerField()
    infovisi_situn = models.CharField(max_length=100)
    infovisit_situf = models.CharField(max_length=100)
    infovisit_intervencion = models.CharField(max_length=200)
    infovisit_compromiso = models.CharField(max_length=200)
    infovisit_citabiblica = models.CharField(max_length=200)
    infovisit_petioracion = models.CharField(max_length=200)
    infovisit_observacion = models.CharField(max_length=200)
    infovisit_nomvisi = models.CharField(max_length=100, blank=True, null=True)
    infovisit_cargo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'informacionvisita'


class Integrantes(models.Model):
    inte_id = models.IntegerField(primary_key=True)
    hog = models.ForeignKey(Hogares, models.DO_NOTHING)
    inte_nombre = models.CharField(max_length=100)
    inte_rol = models.CharField(max_length=100)
    inte_escuidador = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'integrantes'


class Lecciones(models.Model):
    lecc_id = models.IntegerField(primary_key=True)
    marco_id = models.IntegerField()
    lecc_palclave = models.CharField(max_length=50)
    lecc_ideacentral = models.CharField(max_length=50)
    lecc_aspecp = models.CharField(max_length=50)
    lecc_reflper = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'lecciones'


class Log(models.Model):
    log_id = models.IntegerField(primary_key=True)
    usu = models.ForeignKey('Usuario', models.DO_NOTHING)
    mod = models.ForeignKey('Modulos', models.DO_NOTHING)
    log_actividad = models.CharField(max_length=80)
    log_datos = models.CharField(max_length=80)
    log_fechora = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'log'


class MarcoReferencial(models.Model):
    marco = models.OneToOneField('Tutores', models.DO_NOTHING, primary_key=True)
    tipom = models.ForeignKey('Tipomarco', models.DO_NOTHING)
    marco_area = models.CharField(max_length=50)
    marco_tutor = models.CharField(max_length=50)
    marco_fecha = models.DateField()
    marco_refpersonal = models.CharField(max_length=50)
    marco_observacion = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'marco_referencial'


class Marcodereferencia(models.Model):
    marcoref_id = models.IntegerField(primary_key=True)
    plant = models.ForeignKey('Plantilla', models.DO_NOTHING)
    marco_id = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'marcodereferencia'





class Modulos(models.Model):
    mod_id = models.IntegerField(primary_key=True)
    mod_nombre = models.CharField(max_length=50)
    mod_etiqueta = models.CharField(max_length=50)
    mod_ruta = models.CharField(max_length=50)
    esta = models.ForeignKey(Estados, models.DO_NOTHING)
    mod_nucleo = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'modulos'


class Motivoregalo(models.Model):
    mot_id = models.IntegerField(primary_key=True)
    mot_nombre = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'motivoregalo'


class Ocupacionmadre(models.Model):
    ocumadre_id = models.IntegerField(db_column='Ocumadre_id', primary_key=True)  # Field name made lowercase.
    ocumadre_descrip = models.CharField(db_column='Ocumadre_descrip', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ocupacionmadre'


class Ocupacionpadre(models.Model):
    ocupadre_id = models.IntegerField(db_column='OcuPadre_id', primary_key=True)  # Field name made lowercase.
    ocupadre_descrip = models.CharField(db_column='OcuPadre_descrip', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ocupacionpadre'


class Perfiles(models.Model):
    perf_id = models.IntegerField(primary_key=True)
    usu_perfil = models.IntegerField()
    perf_nombre = models.CharField(max_length=50)
    perf_descripcion = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'perfiles'


class Permisos(models.Model):
    perm_id = models.IntegerField(primary_key=True)
    perm_nombre = models.CharField(max_length=50)
    perm_descripcion = models.CharField(max_length=50)
    mod = models.ForeignKey(Modulos, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'permisos'


class PermisosPerfiles(models.Model):
    permperf_id = models.IntegerField(primary_key=True)
    perm = models.ForeignKey(Permisos, models.DO_NOTHING)
    perf = models.ForeignKey(Perfiles, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'permisos_perfiles'


class Plantilla(models.Model):
    plant_id = models.CharField(primary_key=True, max_length=50)
    plant_fechora = models.DateField()
    plant_idtipodocumnetal = models.ForeignKey('Tiposdocumentales', models.DO_NOTHING, db_column='plant_idtipodocumnetal')
    plant_ubicacionfisica = models.CharField(max_length=100)
    plant_idusuariogenera = models.IntegerField()
    plant_idusuariofirma = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'plantilla'


class Rangoingresos(models.Model):
    ingre_id = models.IntegerField(primary_key=True)
    ing_desc = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'rangoingresos'


class Regaloentregado(models.Model):
    regentreg_id = models.IntegerField(primary_key=True)
    entregalo = models.ForeignKey(Entregaregalo, models.DO_NOTHING)
    regentreg_descripcion = models.CharField(max_length=100)
    regentreg_regalo = models.CharField(max_length=100)
    regentreg_nombrecibe = models.CharField(max_length=100)
    mot = models.ForeignKey(Motivoregalo, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'regaloentregado'


class Regalopendiente(models.Model):
    regpend_id = models.IntegerField(primary_key=True)
    entregalo = models.ForeignKey(Entregaregalo, models.DO_NOTHING)
    regpend_descripcion = models.CharField(max_length=200)
    regpend_explicacionnoentrega = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'regalopendiente'






class Situacionlaboralpadre(models.Model):
    sitlabpadre_id = models.IntegerField(primary_key=True)
    sitlabpadre_desc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'situacionlaboralpadre'


class Tipomarco(models.Model):
    tipom_id = models.IntegerField(primary_key=True)
    tipom_nombre = models.CharField(max_length=50)
    tipom_descripcion = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'tipomarco'


class Tiposdocumentales(models.Model):
    tipdoc_id = models.IntegerField(primary_key=True)
    tipdoc_nombre = models.CharField(max_length=50)
    tipdoc = models.TextField()

    class Meta:
        managed = True
        db_table = 'tiposdocumentales'


class Tutores(models.Model):
    tutor_id = models.IntegerField(primary_key=True)
    tutor_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'tutores'


class Usuario(models.Model):
    usu_id = models.IntegerField(primary_key=True)
    usu_perfil = models.IntegerField()
    usu_nombres = models.CharField(max_length=50)
    usu_apellidos = models.CharField(max_length=50)
    usu_email = models.CharField(max_length=50)
    car = models.ForeignKey(Cargos, models.DO_NOTHING)
    usu_usu = models.CharField(max_length=50)
    usu_password = models.CharField(max_length=50)
    esta = models.ForeignKey(Estados, models.DO_NOTHING)
    usu_isadmin = models.TextField()  # This field type is a guess.
    usu_ultsesion = models.DateTimeField()
    usu_fecreacion = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'usuario'


class Visitas(models.Model):
    visit_id = models.IntegerField(primary_key=True)
    plant = models.ForeignKey(Plantilla, models.DO_NOTHING)
    infovisi_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'visitas'
