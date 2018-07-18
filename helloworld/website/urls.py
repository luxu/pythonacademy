from website.views import IndexTemplateView, ComercioListView, ComercioCreateView, \
    ComercioUpdateView, ComercioDeleteView, GastoListView, GastoCreateView, \
    GastoUpdateView, GastoDeleteView

from django.urls import path

urlpatterns = [
    # GET /
    path('',
        IndexTemplateView.as_view(),
        name="index"
    ),

# >>>>>>>>>>>>>>>>>>>> C O M E R C I O <<<<<<<<<<<<<<<<<<<<<<<<<<

    # GET /comercios
    path('comercios/',
        ComercioListView.as_view(),
        name="lista_comercios"
    ),

    # GET /comercio/cadastrar
    path('comercio/cadastrar',
        ComercioCreateView.as_view(),
        name="cadastra_comercio"
    ),

    # GET/POST /comercio/{slug}
    path('comercio/<slug>',
        ComercioUpdateView.as_view(),
        name="atualiza_comercio"
    ),

    # GET/POST /Comercio/excluir/{slug}
    path('comercio/excluir/<slug>',
        ComercioDeleteView.as_view(),
        name="deleta_comercio"
    ),

# >>>>>>>>>>>>>>>>>>>> G A S T O <<<<<<<<<<<<<<<<<<<<<<<<<<

    # GET /gastos
    path('gastos/',
        GastoListView.as_view(),
        name="lista_gastos"
    ),

    # GET /gasto/cadastrar
    path('gasto/cadastrar',
        GastoCreateView.as_view(),
        name="cadastra_gasto"
    ),

    # GET/POST /gasto/{pk}
    path('gasto/<pk>',
        GastoUpdateView.as_view(),
        name="atualiza_gasto"
    ),

    # GET/POST /gasto/excluir/{pk}
    path('gasto/excluir/<pk>',
        GastoDeleteView.as_view(),
        name="deleta_gasto"
    ),
]
