from django.urls import path
from .views import EmpresaCreateView, EmpresaUpdateView

urlpatterns = [
    path('ins', EmpresaCreateView.as_view(), name='create_empresa'),
    path('upd/<int:pk>/', EmpresaUpdateView.as_view(), name='update_empresa'),
]