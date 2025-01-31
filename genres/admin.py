from django.contrib import admin
from genres.models import Genre
from actors.models import Actor


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')