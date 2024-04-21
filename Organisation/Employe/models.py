from django.db import models



class Departements(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nomdept = models.CharField(db_column='NomDEPT', max_length=100)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departements'


class Employes(models.Model):
    id = models.OneToOneField(Departements, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    nomemp = models.CharField(db_column='Nomemp', max_length=100)  # Field name made lowercase.
    prenomemp = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    statut = models.CharField(max_length=20, blank=True, null=True)
    ddn = models.DateField(db_column='DDN', blank=True, null=True)  # Field name made lowercase.
    salaire = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dateembauche = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employes'
