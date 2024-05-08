from django.contrib import admin
from .models import TiposExames, SolicitacaoExames, PedidosExames

admin.site.register(TiposExames)
admin.site.register(SolicitacaoExames)
admin.site.register(PedidosExames)


