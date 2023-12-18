from django.shortcuts import render, redirect
from sa5_app.models import Pessoa

# Create your views here.
def index (request):
    data = Pessoa.objects.all()
    return render(request,"sa5_app/index.html", context={'dados':data})

def salvar(request):
    if request.POST:
        if request.POST["nome"]:
            Pessoa.objects.create(nome = request.POST['nome'])
    return redirect(index)

def deletar(request,id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(app_deletar)

def atualizar(request,id):
    pessoa = Pessoa.objects.get(id=id)
    if request.POST.get("nome"):
        pessoa.nome = request.POST.get("nome")
        pessoa.save()
        return redirect(app_atualizar)
    return render(request,"sa5_app/atualizar.html", context={'dados':pessoa})

def pesquisar(request):
    if request.POST:
        nome = request.POST.get('nome')
        pessoa = [Pessoa.objects.get(nome = nome)]
    else:
        pessoa = Pessoa.objects.all()
    return render(request,"sa5_app/pesquisar.html",context={"dados":pessoa})

def app_deletar(request):
    if request.POST:
        nome = request.POST.get('nome')
        pessoa = [Pessoa.objects.get(nome = nome)]
    else:
        pessoa = Pessoa.objects.all()
    return render(request,"sa5_app/deletar.html",context={"dados":pessoa})

def app_atualizar(request):
    if request.POST:
        nome = request.POST.get('nome')
        pessoa = [Pessoa.objects.get(nome = nome)]
    else:
        pessoa = Pessoa.objects.all()
    return render(request,"sa5_app/atual.html",context={"dados":pessoa})

def app_criar(request):
    nome = ""
    if request.POST:
        nome = request.POST.get('nome')
        if nome:
            Pessoa.objects.create(nome = nome)
    return render(request,"sa5_app/criar.html",context={"pessoa":nome})

def home(request):
    pessoa = Pessoa.objects.all()
    
    return render(request,"sa5_app/home.html",context={"dados":pessoa})


