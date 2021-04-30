from django.shortcuts import render

# Create your views here.

def hello_blog(request):
    lista = [
        'Django','Python','Git','Html',
        'banco de dados', 'Linus', 'Nginx','Uwsgi',
        'Systemctl'
    ]
    data = {'name': 'Curso de Django 3','lista_tecnologias': lista}
    return  render(request,"index.html", data)
    
