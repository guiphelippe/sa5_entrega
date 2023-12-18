from django.urls import path
from sa5_app.views import index, salvar, deletar, atualizar, pesquisar, app_deletar, app_atualizar, app_criar, home

urlpatterns = [
    path('', index),
    path('salvar/', salvar, name='salvar'),
    path('deletar/<int:id>', deletar, name='deletar'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),

    path('app/pesquisar/', pesquisar, name='pesquisar'),
    path('app/deletar/', app_deletar, name='app_deletar'),
    path('app/atualizar/', app_atualizar, name='app_atualizar'),
    path('app/criar/', app_criar, name='app_criar'),
    path('app/home/', home, name='app_home'),
]

