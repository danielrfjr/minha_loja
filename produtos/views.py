from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto # importei do arquivo models, pois antes não estava importado.

def cadastrar_produto(request):
    form = ProdutoForm(request.POST) 
    if form.is_valid():
        form.save()
        return redirect('listar_produto')  
    return render(request, 'cadastro.html', {'form': form})

def listar_produto(request):
    produtos = Produto.objects.all()  # a correção foi mudar produto.objects.all() para Produto.objects.all()
    return render(request, 'listar.html', {'produtos': produtos})
