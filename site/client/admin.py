# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from .output import *

# DISABLE DELETE ALL

admin.site.disable_action('delete_selected')

class BaseAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    ordering = ('name',)   
    exclude = ('slug',)
    
class GeneaAdmin(BaseAdmin):
    list_display = ('name',) 
    
admin.site.register(Genea, GeneaAdmin)

class CongregaAdmin(BaseAdmin):
    list_display = ('name',) 
    
admin.site.register(Congrega, CongregaAdmin)

class PregioDifettoAdmin(BaseAdmin):
    list_display = ('name',) 
    
admin.site.register(PregioDifetto, PregioDifettoAdmin)

class PotereAdmin(BaseAdmin):
    list_display = ('name',) 
    
admin.site.register(Potere, PotereAdmin)

class GiocatoreAdmin(BaseAdmin):
    list_display = ('name', 'user')  
    autocomplete_fields = ('user', )
    
admin.site.register(Giocatore, GiocatoreAdmin)

### PERSONAGGIO    

class PregioInline(admin.TabularInline):
    model = PregioPersonaggioRel
    autocomplete_fields = ('pregio', )
    extra = 0
    
class PotereInline(admin.TabularInline):
    model = PoterePersonaggioRel
    autocomplete_fields = ('potere', )
    extra = 0   

class GuadagnoPXInline(admin.TabularInline):
    model = GuadagnoPX
    readonly_fields = ('px_tot', 'px_fissi')
    autocomplete_fields = ('evento', 'personaggio')
    extra = 0 
    
class SpesaPXInline(admin.TabularInline):
    model = SpesaPX
    autocomplete_fields = ('evento', 'personaggio')
    extra = 0                
    
class SpecManualitaInline(admin.TabularInline):
    model = SpecManualita
    extra = 0     

class PersonaggioAdmin(BaseAdmin):
    list_display = ('name', 'png', 'giocatore', 'genea', 'congrega', 'px_tot', 'px_liberi', 'aetas', 'canal', 'essenza_c', 'voluntas_c')
    search_fields = ('name', 'png', 'active')    
    readonly_fields = ('px_tot', 'px_liberi', 'aetas', 'essenza', 'canal', 'raptus')
    autocomplete_fields = ('giocatore', 'genea', 'congrega')
    fieldsets = (
        ('GENERALE', {
            'fields': (('name', 'giocatore', 'active'), ('genea', 'congrega', 'png'),)
        }),
        ('STATO', {
            'fields': (('essenza_c', 'voluntas_c', 'carica'),)
        }),        
        ('SPECIALE', {
            'fields': (('px_tot', 'px_liberi', 'aetas', 'essenza', 'canal', 'raptus', 'voluntas', 'aetas_base'), )
        }),        
        ('ATTRIBUTI', {
            'fields': (('vigore', 'destrezza', 'psiche', 'percezione', 'nefesh',   'persuasione'),)
        }),
        ('CAPACITA', {
            'fields': (('armi_fuoco', 'atletica', 'manualita', 'armi_bianche', 'sopravvivenza'),)
        }),    
        ('CONOSCENZE', {
            'fields': (('accademiche', 'economia', 'legge', 'ritualistica', 'strada'),)
        }),    
        ('INFLUENZE', {
            'fields': (('alta_societa', 'finanza', 'politica', 'occultismo', 'criminalita'), ('sanita', 'trasporti', 'forze_ordine', 'religione','media'))
        }),              
        ('BACKGROUND', {
            'fields': (('risorse', 'mentore', 'gregge', 'retaggio', 'discepoli', 'alleati'),)
        }),       
        ('VARIO', {
            'fields': ('dichiarazione', )
        }),                                   

    )
    inlines = [SpecManualitaInline, PregioInline, PotereInline, GuadagnoPXInline, SpesaPXInline]
    actions = [print_scheda]
      
    class Media:   
        css = {
             'all': ('/static/client/extra.css ',)
        }      
    
admin.site.register(Personaggio, PersonaggioAdmin)

class EventoAdmin(BaseAdmin):
    list_display = ('name',) 
    ordering = ('data',)  
    inlines = [GuadagnoPXInline, SpesaPXInline]
    
admin.site.register(Evento, EventoAdmin)
