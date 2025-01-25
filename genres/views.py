import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genre


@csrf_exempt     # -----> Decorator de excessão do csrf token, necessário para autorizar o POST
def genre_view(request):
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