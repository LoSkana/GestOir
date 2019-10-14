from django.shortcuts import render
import datetime
from django.http import HttpResponse, Http404, FileResponse
from .models import *

def nice_try(request):
    return render(request, 'client/nice_try.html')

def index(request):
    cxt = {}
    cxt['pl'] = request.user.giocatore
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
        
def px(request, idx):
    try:
        cxt = {'pg': Personaggio.objects.get(pk=idx)}
        if cxt['pg'].giocatore != request.user.giocatore:
            return nice_try(request)
            
        return render(request, 'client/px.html', cxt)
    except Personaggio.DoesNotExist:
        return nice_try(request)
         
 