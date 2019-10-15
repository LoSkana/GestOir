from django.http import HttpResponse

from django.conf import settings

import datetime
import os
import textwrap

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from slugify import slugify

pdfmetrics.registerFont(TTFont('Balthazar', os.path.join(settings.SCHEDE_DIR, 'Balthazar.ttf')))

from reportlab.rl_config import defaultPageSize

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]

def print_scheda(modeladmin, request, queryset):    
    response = HttpResponse(content_type='application/pdf')    
    
    if len(queryset) == 1:
        title = slugify(queryset[0].name)
    else:
        title = "%s-%s" % ('Schede OiR', datetime.date.today())
        
    response['Content-Disposition'] = 'attachment; filename=%s.pdf' % (title, )
        
    output = PdfFileWriter()
 
    for pg in queryset:
        print_scheda_pg(pg)
        pdf_reader = PdfFileReader(os.path.join(settings.SCHEDE_DIR, "all", pg.secret + ".pdf"))
        for page in range(pdf_reader.getNumPages()):
            output.addPage(pdf_reader.getPage(page))       
            
    outputStream = response
    output.write(response)
    outputStream.close()
    
    return response
    
print_scheda.short_description = "Stampa scheda"

def s(i):
    if i == 0:
        return ''
    else:
        return str(i)

def ss(i):
    if i > 0:
        return '+%d' % (i, )
    else:
        return str(i)
        

def print_scheda_pg(pg):
    
    # create a new PDF with Reportlab
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    
    # write detail of the scheda
    can.setFont('Balthazar', 26)
    can.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-57, pg.name)
    
    can.setFont('Balthazar', 20)
    can.drawCentredString(170, PAGE_HEIGHT-83, "%s / %s" % (pg.genea, pg.congrega))
    can.drawCentredString(430, PAGE_HEIGHT-83, "%s" % (pg.giocatore, )) 
    
    can.setFont('Balthazar', 14)
    w_attr = 254
    w_spec = 506
    y_first = 116
    y_incr = 24.8
    
    w_pos = w_attr
    y_pos = y_first
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%d" % (pg.vigore, )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%d" % (pg.destrezza, )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%d" % (pg.psiche, ))     
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%d" % (pg.percezione, ))   
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%d" % (pg.nefesh, ))    
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%d" % (pg.persuasione, )) 
    
    w_pos = w_spec
    y_pos = y_first
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%d" % (pg.aetas, )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%d" % (pg.essenza, )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%d" % (pg.canal, ))     
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%d" % (pg.voluntas, ))   
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%d" % (pg.raptus, ))    
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (pg.carica, )) 
    
    w_cap = 155
    w_con = 273
    w_inf = 415
    w_bgk = 538
    y_second = 324
   
    y_incr = 23.4
    
    w_pos = w_cap
    y_pos = y_second
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.armi_fuoco), )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.atletica), )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.manualita), ))     
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.armi_bianche), ))   
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.sopravvivenza), ))      
    
    w_pos = w_inf
    y_pos = y_second
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.alta_societa), )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.sanita), )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.finanza), ))     
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.trasporti), ))   
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.politica), ))
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.forze_ordine), )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.occultismo), ))     
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.religione), ))   
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.criminalita), ))
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.media), ))     
    
    w_pos = w_bgk
    y_pos = y_second
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.risorse), )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.mentore), )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.gregge), ))     
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.retaggio), ))   
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.discepoli), ))    
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.alleati), ))  
    
    w_pos = w_con
    y_incr = y_incr * 2
    y_pos = y_second + y_incr / 2 - 11
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.accademiche), )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.economia), )) 
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.legge), ))     
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.ritualistica), ))   
    y_pos += y_incr
    can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (s(pg.strada), ))     
    
    y_spec = 482
    w_spec = 95  
    
    y_incr = 23.1
    
    w_pos = w_spec
    y_pos = y_spec
    for obj in pg.spec_manualita.all():        
        can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s (%d)" % (obj.name,  obj.livello ))      
        y_pos += y_incr   
        # print(obj)
        
    y_third = 595
    w_pregi = 150        
    
    w_pos = w_pregi
    y_pos = y_third
    for obj in pg.pregi.all():        
        can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (obj.pregio, ))      
        can.drawCentredString(w_pos + 120, PAGE_HEIGHT-y_pos, "%s" % (ss(obj.bonus, ))  )
        y_pos += y_incr       
        
    w_poteri = 420        
    
    w_pos = w_poteri
    y_pos = y_third
    for obj in pg.poteri.all():        
        can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, "%s" % (obj.potere, ))      
        can.drawCentredString(w_pos + 120, PAGE_HEIGHT-y_pos, "%s" % (obj.livello, ))  
        y_pos += y_incr                 
    
    w_dichiaraz = 165
    y_dichiaraz = 785     
    
    # can.drawCentredString(w_dichiaraz, PAGE_HEIGHT-y_dichiaraz, "ciao")    
    
    lines = textwrap.wrap(pg.dichiarazione, 40, break_long_words=False)
    
    w_pos = w_dichiaraz
    y_incr = y_incr / 2
    y_pos = y_dichiaraz - y_incr * len(lines) / 2.4
    for l in lines:     
        can.drawCentredString(w_pos, PAGE_HEIGHT-y_pos, l)      
        y_pos += y_incr      
                
    
    # save the canvas
    can.save()
    
    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open(os.path.join(settings.SCHEDE_DIR, "scheda.pdf"), "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    
    pdf_path = os.path.join(settings.SCHEDE_DIR, "all", pg.secret + ".pdf")
    if os.path.exists(pdf_path):
        os.remove(pdf_path)    
    outputStream = open(pdf_path, "wb")
    output.write(outputStream)
    outputStream.close()
 

def update_pg(pg):
    pg.px_tot = 0
    for obj in pg.guadagni.all():     
        pg.px_tot += obj.px_tot
   
    pg.px_liberi = pg.px_tot
    for obj in pg.spese.all():     
        pg.px_liberi -= obj.px_spesi
        
    pg.aetas = int(pg.aetas_base + pg.px_tot / 10)
    pg.canal = int(pg.aetas / 6)
    pg.essenza = int(pg.aetas * ( 1.5 + 0.5 * pg.retaggio))
    
    pg.raptus = pg.retaggio + pg.nefesh
    
    if pg.essenza_c == 0:
        pg.essenza_c = pg.essenza

    if pg.voluntas_c == 0:
        pg.voluntas_c = pg.voluntas
    
    print_scheda_pg(pg)
    
    # print("ciao")
