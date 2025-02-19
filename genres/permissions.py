#--------------------------NÃO É MAIS UTILIZADO-----------------------------------------------

from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):    # ----> Polimorfismo do método importado de permissions
        if request.method in ['GET', 'OPTIONS', 'HEAD']:    # ----> Se for um get, options ou head, verifica se usuário possui permissão para visualizar gêneros
            return request.user.has_perm('genres.view_genre')
        
        if request.method == 'POST':    # ----> Se for um post, verifica se usuário possui permissão para criar gêneros
            return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PATCH', 'PUT']:    # ----> Se for um put ou patch, verifica se usuário possui permissão para modificar gêneros
            return request.user.has_perm('genres.change_genre')
        
        if request.method == 'DELETE':    # ----> Se for um delete, verifica se usuário possui permissão para deletar gêneros
            return request.user.has_perm('genres.delete_genre')

        return False