from django.contrib import admin
from .models import Animal, Raca, TipoGranja, FaseProducao, Localizacao, Granja

admin.site.register(Granja)
admin.site.register(Animal)
admin.site.register(Raca)
admin.site.register(TipoGranja)
admin.site.register(FaseProducao)
admin.site.register(Localizacao)