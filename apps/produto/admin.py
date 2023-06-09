from django.contrib import admin
from produto.models import Produto, Variacao, Categoria



class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 0

class ProdutoAdmin(admin.ModelAdmin):
    inlines = [VariacaoInline]

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
admin.site.register(Categoria)


