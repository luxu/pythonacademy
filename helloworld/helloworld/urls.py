from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import login, logout

from core import views

urlpatterns = [
    # URL padrão
    path('', views.index, name='index'),
    path('entrar/', login, {'template_name':'login.html'}, name='login'),
    path('sair/', logout, {'next_page':'index'}, name='logout'),
    # path('sair/', include({'next_page':'index'})),
    # path('website/', include('website.urls', namespace='website')),
    path('conta/', include('accounts.urls')),
    # Interface administrativa
    path('admin/', admin.site.urls),
]
