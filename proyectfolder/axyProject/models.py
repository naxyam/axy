# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actividadescristianas(models.Model):
    activcris_id = models.AutoField(primary_key=True)
    activcris_nombre = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'actividadescristianas'


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
    benef_activcrist = models.ForeignKey(Actividadescristianas, models.DO_NOTHING, db_column='benef_activcrist')

    class Meta:
        managed = True
        db_table = 'beneficiario'


class Cargos(models.Model):
    car_id = models.IntegerField(primary_key=True)
    car_nombre = models.CharField(max_length=50)
    car_desc = models.CharField(max_length=50)
    esta = models.ForeignKey('Estados', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'cargos'


class Ciudades(models.Model):
    ciu_id = models.AutoField(primary_key=True)
    ciu_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'ciudades'


class Deberes(models.Model):
    deb_id = models.AutoField(primary_key=True)
    deb_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'deberes'


class Deberesxbenef(models.Model):
    debxben_id = models.IntegerField(primary_key=True)
    debxben_idben = models.ForeignKey(Beneficiario, models.DO_NOTHING, db_column='debxben_idben', blank=True, null=True)
    debxben_iddeb = models.ForeignKey(Deberes, models.DO_NOTHING, db_column='debxben_iddeb', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'deberesxbenef'


class Departamento(models.Model):
    dep_id = models.AutoField(primary_key=True)
    dep_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'departamento'


class Discapacidadesfisicas(models.Model):
    disfisica_id = models.IntegerField(primary_key=True)
    disfisica_nombre = models.CharField(max_length=100)
    disfisica_descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'discapacidadesfisicas'


class Discapacidadesmentales(models.Model):
    dismental_id = models.IntegerField(primary_key=True)
    dismental_nombre = models.CharField(max_length=100)
    dismental_descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'discapacidadesmentales'


class Disfisicaxhistoria(models.Model):
    disfixhist_id = models.IntegerField(primary_key=True)
    disfixhist_disfisicaid = models.ForeignKey(Discapacidadesfisicas, models.DO_NOTHING, db_column='disfixhist_disfisicaid')
    disfixhist_historiaid = models.ForeignKey('Historiaclinica', models.DO_NOTHING, db_column='disfixhist_historiaid')

    class Meta:
        managed = True
        db_table = 'disfisicaxhistoria'


class Dismentalxhistoria(models.Model):
    dismenxhist_id = models.IntegerField(primary_key=True)
    dismenxhist_dismenid = models.ForeignKey(Discapacidadesmentales, models.DO_NOTHING, db_column='dismenxhist_dismenid')
    dismenxhist_historiaid = models.ForeignKey('Historiaclinica', models.DO_NOTHING, db_column='dismenxhist_historiaid')

    class Meta:
        managed = True
        db_table = 'dismentalxhistoria'


class Educacionformal(models.Model):
    eformal_id = models.IntegerField(primary_key=True)
    eformal_nombre = models.CharField(max_length=100)
    eformal_descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'educacionformal'


class Enfcronicaxhistoria(models.Model):
    enfcronicaxhist_id = models.IntegerField(primary_key=True)
    enfcronicaxhist_disfisicaid = models.ForeignKey('Enfermedadcronica', models.DO_NOTHING, db_column='enfcronicaxhist_disfisicaid')
    enfcronicaxhist_historiaid = models.ForeignKey('Historiaclinica', models.DO_NOTHING, db_column='enfcronicaxhist_historiaid')

    class Meta:
        managed = True
        db_table = 'enfcronicaxhistoria'


class Enfermedadcronica(models.Model):
    enfcronica_id = models.IntegerField(primary_key=True)
    enfcronica_nombre = models.CharField(max_length=100)
    enfcronica_descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'enfermedadcronica'


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


class Grupoetareo(models.Model):
    grupeta_id = models.IntegerField(primary_key=True)
    grupeta_nombre = models.CharField(max_length=100)
    grupeta_descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'grupoetareo'


class Historiaclinica(models.Model):
    histclinica_id = models.IntegerField(primary_key=True)
    histclinica_beneid = models.ForeignKey(Beneficiario, models.DO_NOTHING, db_column='histclinica_beneid', blank=True, null=True)
    histclinica_peso = models.FloatField(blank=True, null=True)
    histclinica_talla = models.FloatField(blank=True, null=True)
    histclinica_tratmedico = models.TextField(db_column='histclinica_tratMedico', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'historiaclinica'


class Hobbies(models.Model):
    hob_id = models.AutoField(primary_key=True)
    hob_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'hobbies'


class Hobbiesxbenef(models.Model):
    hobxben_id = models.IntegerField(primary_key=True)
    hobxben_idben = models.ForeignKey(Beneficiario, models.DO_NOTHING, db_column='hobxben_idben', blank=True, null=True)
    hobxben_idhob = models.ForeignKey(Hobbies, models.DO_NOTHING, db_column='hobxben_idhob', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hobbiesxbenef'


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


class Materias(models.Model):
    mat_id = models.AutoField(primary_key=True)
    mat_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'materias'


class Materiasxbenef(models.Model):
    matxben_id = models.IntegerField(primary_key=True)
    matxben_idben = models.ForeignKey(Beneficiario, models.DO_NOTHING, db_column='matxben_idben', blank=True, null=True)
    matxben_idmat = models.ForeignKey(Materias, models.DO_NOTHING, db_column='matxben_idmat', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'materiasxbenef'


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


class Religion(models.Model):
    rel_id = models.AutoField(primary_key=True)
    rel_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'religion'


class Rendimientoacademico(models.Model):
    rendiaca_id = models.AutoField(primary_key=True)
    rendiaca_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'rendimientoacademico'


class Sexo(models.Model):
    sex_id = models.AutoField(primary_key=True)
    sex_nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'sexo'


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
