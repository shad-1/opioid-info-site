
from django.db import models

class PdDrug(models.Model):
    drugid = models.AutoField(primary_key=True, db_column='drugid')
    drugname = models.CharField(max_length=30)
    isopioid = models.BooleanField()

    class Meta:
        db_table = 'pd_drug'

    def __str__(self):
        return self.drugname


class PdStatedata(models.Model):
    state = models.CharField(max_length=14, db_column='state')
    stateabbrev = models.CharField(primary_key=True, max_length=2)
    population = models.IntegerField()
    deaths = models.IntegerField()

    class Meta:
        db_table = 'pd_statedata'

    def __str__(self):
        return self.state
    


class PdPrescriber(models.Model):
    npi = models.BigIntegerField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    state = models.ForeignKey(PdStatedata, on_delete=models.DO_NOTHING, db_column='state')
    specialty = models.CharField(max_length=200)
    isopioidprescriber = models.BooleanField()
    totalprescriptions = models.IntegerField()

    class Meta:
        db_table = 'pd_prescriber'
        
    def __str__(self):
        return self.fname + ' ' + self.lname

class PdCredential(models.Model):
    npi = models.BigIntegerField(primary_key=True)
    credential = models.CharField(max_length=20)

    class Meta:
        db_table = 'pd_credential'
        unique_together = (('npi', 'credential'),)

class PdPrescriptionquantity(models.Model):
    npi = models.BigIntegerField(primary_key=True)
    drugid = models.ForeignKey(PdDrug, on_delete=models.DO_NOTHING, db_column="drugid")
    quantity = models.IntegerField()

    class Meta:
        db_table = 'pd_prescriptionquantity'
        unique_together = (('npi', 'drugid'),)
        managed = False


class PdTriple(models.Model):
    id = models.AutoField(primary_key=True)
    prescriberid = models.BigIntegerField()
    drugname = models.CharField(max_length=30)
    qty = models.IntegerField()

    class Meta:
        db_table = 'pd_triple'
        managed = False
