from django.urls import path
from .views import FuncionariosListView, FuncionarioUpdateView, FuncionarioDeleteView, FuncionarioCreateView

urlpatterns = [
    path('', FuncionariosListView.as_view(), name='list_funcionarios'),
    path('ins/', FuncionarioCreateView.as_view(), name='create_funcionario'),
    path('upd/<int:pk>/', FuncionarioUpdateView.as_view(), name='update_funcionario'),
    path('del/<int:pk>/', FuncionarioDeleteView.as_view(), name='delete_funcionario'),
]