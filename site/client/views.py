from django.shortcuts import render
import datetime
from django.http import HttpResponse, Http404, FileResponse
from .models import *
from slugify import slugify

def nice_try(request):
    return render(request, 'client/nice_try.html')

def index(request):
    cxt = {}
    try: 
        cxt['pl'] = request.user.giocatore
    except Exception:
        return render(request, 'client/none.html', cxt) 
    if cxt['pl'] is None: 
        return render(request, 'client/none.html', cxt)

    cxt['pgs'] = cxt['pl'].personaggi.all()
    return render(request, 'client/index.html', cxt)
    
def sheet(request, idx):
    try:
        cxt = {'pg': Personaggio.objects.get(pk=idx)}
        if cxt['pg'].giocatore != request.user.giocatore:
            return nice_try(request)
        
        print(cxt['pg'].secret + ".pdf")
        try:
            response = FileResponse(open(os.path.join(settings.SCHEDE_DIR, "all", cxt['pg'].secret + ".pdf"), 'rb'), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=%s-%s.pdf'% (slugify(cxt['pg'].name), datetime.date.today())
            return response
        except FileNotFoundError:
            raise Http404()        
    except Personaggio.DoesNotExist:
        return nice_try(request)
        
def stato(request, idx):
    try:
        cxt = {'pg': Personaggio.objects.get(pk=idx)}
        if cxt['pg'].giocatore != request.user.giocatore:
            return nice_try(request)
            
        cxt['pg'].bgk = []
        for b in ['risorse', 'mentore', 'gregge', 'retaggio', 'discepoli', 'alleati']:
            v = getattr(cxt['pg'], b)
            if v > 0: 
                el = {'nome': b.capitalize() , 'livello': v}
                cxt['pg'].bgk.append(el)
        
        cxt['pg'].inf = []
        for b in ['alta_societa', 'sanita', 'finanza', 'trasporti', 'politica', 'forze_ordine', 'occultismo', 'religione', 'criminalita', 'media']:
            v = getattr(cxt['pg'], b)
            if v > 0: 
                el = {'nome': b.capitalize() , 'livello': v}
                cxt['pg'].inf.append(el)                
           
        return render(request, 'client/stato.html', cxt)
    except Personaggio.DoesNotExist:
        return nice_try(request)
         
 
