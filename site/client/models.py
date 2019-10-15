import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

from slugify import slugify
import hashlib 
import time

from django.contrib.auth.models import User

from .output import *

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 
    class Meta:
        abstract = True
        
class AdvancedModel(BaseModel):
    slug = models.CharField(max_length=60, unique=True)  

    class Meta:
        abstract = True        
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BaseModel, self).save(*args, **kwargs)        

class Genea(AdvancedModel):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = 'Genee'     
    def __str__(self):
        return self.name        
    
class Congrega(AdvancedModel):
    name = models.CharField(max_length=30)  
    class Meta:
        verbose_name_plural = 'Congreghe'        
    def __str__(self):
        return self.name     
        
class PregioDifetto(AdvancedModel):
    name = models.CharField(max_length=30)  
    class Meta:
        verbose_name_plural = 'Pregi e Difetti'        
    def __str__(self):
        return self.name  
        
class Potere(AdvancedModel):
    name = models.CharField(max_length=30)  
    class Meta:
        verbose_name_plural = 'Poteri'        
    def __str__(self):
        return self.name          
        
class Giocatore(AdvancedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='giocatore', blank=True, null=True)   
    name = models.CharField(max_length=30)  
    class Meta:
        verbose_name_plural = 'Giocatori'        
    def __str__(self):
        return self.name 

def md5secret():
    return hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()

class Personaggio(AdvancedModel):
    giocatore = models.ForeignKey(Giocatore, on_delete=models.SET_NULL, null=True, related_name='personaggi')
    name = models.CharField(max_length=30)
    png = models.BooleanField(default=False)
    genea = models.ForeignKey(Genea, models.SET_NULL, null=True, related_name='genea') 
    congrega = models.ForeignKey(Congrega, models.SET_NULL, null=True, related_name='congrega') 
    px_tot = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(500)])
    px_liberi = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(500)])
    essenza_c  = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)], verbose_name='Essenza corrente') 
    voluntas_c = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name='Voluntas corrente') 
    
    vigore = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    destrezza = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    psiche = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    percezione = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    nefesh = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    persuasione = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    
    aetas  = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    aetas_base = models.SmallIntegerField(default=20, validators=[MinValueValidator(0), MaxValueValidator(100)])
    essenza  = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(200)], verbose_name='Essenza max')
    canal = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    voluntas = models.SmallIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name='Volutantas max')
    raptus = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(15)])
    carica = models.CharField(max_length=30, blank=True)
    
    armi_fuoco = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    atletica = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    manualita = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    armi_bianche = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    sopravvivenza = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])  
    
    accademiche = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    economia = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    legge = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    ritualistica = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    strada = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    alta_societa = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    sanita = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    finanza = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    trasporti = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    politica = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    forze_ordine = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    occultismo = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    religione = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    criminalita = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    media = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    risorse = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    mentore = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    gregge = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    retaggio = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    discepoli = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    alleati = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    dichiarazione = models.CharField(max_length=300, blank=True)
    
    secret = models.CharField(max_length=32, unique=True, default=md5secret)
    
    class Meta:
        verbose_name_plural = 'Personaggi'  
        
    def __str__(self):
        return self.name            
        
@receiver(pre_save, sender=Personaggio)
def personaggio_save(sender, instance, **kwargs):  
    update_pg(instance)    

class PregioPersonaggioRel(BaseModel):
    pregio = models.ForeignKey(PregioDifetto, on_delete=models.CASCADE, related_name='personaggi')
    personaggio = models.ForeignKey(Personaggio, on_delete=models.CASCADE, related_name='pregi')
    bonus = models.SmallIntegerField(default=0, validators=[MinValueValidator(-10), MaxValueValidator(10)])
    dettagli = models.CharField(max_length=20, blank=True)
    
    class Meta:
        verbose_name_plural = 'Pregi e Difetti'    
        unique_together = ('pregio', 'personaggio',) 
    def __str__(self):
        return "%s - %s - %d" % (self.personaggio, self.pregio, self.bonus)  
        
class SpecManualita(BaseModel):
    personaggio = models.ForeignKey(Personaggio, on_delete=models.CASCADE, related_name='spec_manualita')
    name = models.CharField(max_length=30)
    livello = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    class Meta:
        verbose_name_plural = 'Specializzazione manualita' 
        unique_together = ('name', 'personaggio',)     
    def __str__(self):
        return "%s - %s - %d" % (self.personaggio, self.name, self.livello)                    
    
class PoterePersonaggioRel(BaseModel):
    potere = models.ForeignKey(Potere, on_delete=models.CASCADE, related_name='personaggi')
    personaggio = models.ForeignKey(Personaggio, on_delete=models.CASCADE, related_name='poteri')
    livello = models.SmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    
    class Meta:
        verbose_name_plural = 'Poteri'   
        unique_together = ('potere', 'personaggio',)  
    def __str__(self):
        return "%s - %s - %d" % (self.personaggio, self.potere, self.livello)         

class Evento(AdvancedModel):
    name = models.CharField(max_length=60)  
    data = models.DateField()
    class Meta:
        verbose_name_plural = 'Eventi'        
    def __str__(self):
        return self.name      

class GuadagnoPX(BaseModel):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='guadagni')
    personaggio = models.ForeignKey(Personaggio, on_delete=models.CASCADE, related_name='guadagni')
    px_tot = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    
    px_fissi = models.SmallIntegerField(default=None, validators=[MinValueValidator(0), MaxValueValidator(20)])    
    interpretazione = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    costumistica = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    qualita_gioco = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    qualita_azioni = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])               
    
    class Meta:
        verbose_name_plural = 'Px Guadagnati'     
        unique_together = ('evento', 'personaggio',)
    
    def __str__(self):
        return "" 
    
    def update_px(self):
        if self.px_fissi is None:
            eventi = self.personaggio.Guadagni.count()
            self.px_fissi = 15 - eventi
        self.px_tot = self.px_fissi + self.interpretazione + self.costumistica + self.qualita_gioco + self.qualita_azioni

@receiver(pre_save, sender=GuadagnoPX)
def guadagno_pre_save(sender, instance, **kwargs):  
    instance.update_px()

@receiver(post_save, sender=GuadagnoPX)
def guadagno_post_save(sender, instance, created, **kwargs):  
    update_pg(instance.personaggio) 
    instance.personaggio.save()            

class SpesaPX(BaseModel):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='spese')
    personaggio = models.ForeignKey(Personaggio, on_delete=models.CASCADE, related_name='spese')
    px_spesi = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(30)])
    motivazione = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'Px Spesi'   
        unique_together = ('evento', 'personaggio',)  
    def __str__(self):
        return ""       

@receiver(post_save, sender=SpesaPX)
def spesa_save(sender, instance, created, **kwargs):  
    update_pg(instance.personaggio) 
    instance.personaggio.save()         
