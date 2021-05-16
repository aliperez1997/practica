from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login 

def index(request):
    return render(request, 'index.html', {
        'mensaje' : 'Listado de Productos',
        'titulo' : 'Productos',
        'products' : [
            {'titulo': 'Camisa' , 'precio' : 5, 'stock': True},
            {'titulo': 'Pantalon' , 'precio' : 20, 'stock': True},
            {'titulo': 'Correa' , 'precio' : 3, 'stock': False},
            {'titulo': 'Chaqueta' , 'precio' : 15, 'stock': True},
            {'titulo': 'Medias' , 'precio' : 1, 'stock': False}
        ]
    })

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username, password=password) 
        if user:
            login(request, user)
            return redirect ('index')


        
    return render(request, 'users/login.html', {

    })