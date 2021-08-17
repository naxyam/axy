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


class BeneAdmin(admin.ModelAdmin):
    readonly_fields=('benef_created', 'benef_updated')

admin.site.register(models.Beneficiario, BeneAdmin)

admin.site.register(models.Hobbies)

admin.site.register(models.Hobbiesxbenef)

admin.site.register(models.Materias)

admin.site.register(models.Materiasxbenef)


admin.site.register(models.Deberes)

admin.site.register(models.Deberesxbenef)



