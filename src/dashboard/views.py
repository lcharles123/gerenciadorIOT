from django.shortcuts import render

from dashboard.models import usuario
    
# views do site 
# from .models import Book, Author, BookInstance, Genre

#view da pagina principal
def dashboard(request):
    #colocar aqui as funcoes para obter os dados dinamicos quando carregados a pagina index, ex. lista de dispositivos
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_visits': num_visits},
    )

