from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PokemonType(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PokemonSpecies(models.Model):

    name = models.CharField(max_length=100)
    evolutionLevel = models.IntegerField(blank=True,null=True, verbose_name='Evolution Level')
    nextEvolution = models.ForeignKey('self',on_delete=models.CASCADE, blank=True, null=True, verbose_name='Next Evolution')
    pokemonType = models.ManyToManyField(PokemonType)

    class Meta:
        verbose_name = 'Pokemon Specie'

    def __str__(self):
        return self.name

class Pokemon(models.Model):

    nickname = models.CharField(max_length=100)
    species = models.ForeignKey(PokemonSpecies,on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    trainer = models.ForeignKey(User,on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        if self.level >= self.species.evolutionLevel:
            species = PokemonSpecies.objects.get(name=self.species.nextEvolution.name)
            self.species = species
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.nickname
