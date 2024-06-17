from django.shortcuts import render, redirect, get_object_or_404
from core.models import Evento
#from models import Evento

# Create your views here.
def index(request):
    return redirect('/agenda/')
def lista_eventos(request):
    #usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()
    data = {'eventos': evento}
    return render(request, 'agenda.html', data)