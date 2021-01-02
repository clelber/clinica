from django.urls import path
from .views import DepartamentosListView, DepartamentoCreateView, DepartamentoUpdateView, DepartamentoDeleteView

urlpatterns = [
    path('', DepartamentosListView.as_view(), name='list_departamentos'),
    path('ins/', DepartamentoCreateView.as_view(), name='create_departamento'),
    path('upd/<int:pk>/', DepartamentoUpdateView.as_view(), name='update_departamento'),
    path('del/<int:pk>/', DepartamentoDeleteView.as_view(), name='delete_departamento'),
]