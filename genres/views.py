import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from genres.models import Genre


@csrf_exempt     # -----> Decorator de excessão do csrf token, necessário para autorizar o POST
def genre_create_list_view(request):
    if request.method == 'GET':     # -----> Quando é GET, retorna do banco a lista de gêneros cadastrados
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':     # -----> Quando é POST, captura os dados do body da request, e armazena no banco de dados
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name},
            status=201,
        )
    

@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':     # -----> Quando recebe um GET com a primary key na url, retorna o objeto em detalhes
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    
    elif request.method == 'PUT':     # -----> Quando recebe um PUT com a primary key na url, retorna para edição do objeto
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            {'id': genre.id, 'name': genre.name}
        )