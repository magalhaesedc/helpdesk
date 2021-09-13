from django import forms
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .forms import ContatoForm
from .models import *


# Create your views here.
# def index(request):
#     return render(request, 'index.html')


def contato(resquest):
    form = ContatoForm()

    context = {
        'form': form
    }
    return render(resquest, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')

def chamado(request):
    return render(request, 'chamado.html')

# def login(request):
#     return render(request, 'login.html')

def index(request):
    chamado_list = Chamado.objects.all()
    paginator = Paginator(chamado_list, 5)

    page = request.GET.get('page')

    chamado = paginator.get_page(page)

    chamados = {'lista': chamado}
    return render(request, 'listar.html', chamados)

def detalhe_chamado(request, id):
    chamado_numero = get_object_or_404(Chamado, pk=id)
    chamado = {'chamado': chamado_numero}
    return render(request, 'detalhe_chamado.html', chamado)

def feedback(request):
    return render(request, 'feedback.html')
