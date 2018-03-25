from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        if request.POST.get('password') == 'teste123':
            return redirect('/index')
        else:
            user = request.POST.get('email')
            content = {"error": "Usuario {} digitou a senha errada!".format(user)}
            return render(request, "login.html", content)
