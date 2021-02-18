from django.contrib import admin
from .models import *

# Register your models here.

class PokemonSpeciesAdmin(admin.ModelAdmin):

    list_display = ['name', 'Evolution_Level', 'Next_Evolution']
    filter_horizontal = ('pokemon_Type',)

admin.site.register(Pokemon)
admin.site.register(PokemonSpecies,PokemonSpeciesAdmin)
admin.site.register(PokemonType)