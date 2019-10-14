from django.db import models

from django.contrib.auth.models import User

class Genea(models.Model):
    name = models.CharField(max_length=30)
    
class Congrega(models.Model):
    name = models.CharField(max_length=30)    

class Personaggio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    genea = models.ForeignKey(Genea, models.SET_NULL, null=True, related_name='Genea') 
    congrega = models.ForeignKey(Congrega, models.SET_NULL, null=True, related_name='Congrega') 
    px_tot = models.IntegerField(default=1)
    px_liberi = models.IntegerField(default=1)
    vigore = models.IntegerField(default=1)
    destrezza = models.IntegerField(default=1)
    psiche = models.IntegerField(default=1)
    percezione = models.IntegerField(default=1)
    nefesh = models.IntegerField(default=1)
    persuasione = models.IntegerField(default=1)
    persuasione = models.IntegerField(default=1)
    aetas  = models.IntegerField(default=1)
    canal = models.IntegerField(default=1)
    voluntas = models.IntegerField(default=1)
    raptus = models.IntegerField(default=1)
    carica = models.CharField(max_length=30)
