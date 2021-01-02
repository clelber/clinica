from django.urls import path
from .views import HoraextraListView

urlpatterns = [
    path('', HoraextraListView.as_view(), name='list_hora_extra'),
]