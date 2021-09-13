from functools import partial
from django.urls import path

from .views import detalhe_chamado, index, contato, produto, chamado, feedback


urlpatterns = [
    #path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    path('chamado/', chamado, name='chamado'),
    # path('login/', login, name='login'),
    path('', index, name='index'),
    path('detalhe_chamado/<int:id>', detalhe_chamado, name='detalhe_chamado'),
    path('feedback/', feedback, name='feedback'),
]