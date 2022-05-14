from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
  list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'rendimento', 'ingredientes')
  list_display_links = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'rendimento', 'ingredientes')
  search_fields = ('nome_receita', 'categoria', 'ingredientes')
  list_filter = ('ingredientes',)
  list_per_page = 2


admin.site.register(Receita, ListandoReceitas)