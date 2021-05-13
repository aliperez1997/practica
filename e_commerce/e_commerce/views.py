from django.shortcuts import render
from django.http import HttpResponse 

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
