from django.contrib import admin
from .models import *

# Register your models here.

class PokemonSpeciesAdmin(admin.ModelAdmin):

    list_display = ['name','evolutionLevel','nextEvolution']
    filter_horizontal = ('pokemonType',)

admin.site.register(Pokemon)
admin.site.register(PokemonSpecies,PokemonSpeciesAdmin)
admin.site.register(PokemonType)