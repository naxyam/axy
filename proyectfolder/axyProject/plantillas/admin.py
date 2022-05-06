from django.contrib import admin
from plantillas import models

# Register your models here.

admin.site.register(models.Sexo)

admin.site.register(models.Religion)

admin.site.register(models.Rendimientoacademico)

admin.site.register(models.Educacionformal)

admin.site.register(models.Grupoetareo)

admin.site.register(models.Actividadescristianas)

admin.site.register(models.Ciudades)

admin.site.register(models.Departamento)

admin.site.register(models.Discapacidadesfisicas)

admin.site.register(models.Discapacidadesmentales)

admin.site.register(models.Enfermedadcronica)


class BeneAdmin(admin.ModelAdmin):
    readonly_fields=('benef_created', 'benef_updated')

admin.site.register(models.Beneficiario, BeneAdmin)

admin.site.register(models.Hobbies)

admin.site.register(models.Materias)

admin.site.register(models.Deberes)





