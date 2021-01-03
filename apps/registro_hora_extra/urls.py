from django.urls import path
from .views import HoraextraListView, HoraextraUpdateView, HoraextraDeleteView, HoraextraCreateView

urlpatterns = [
    path('', HoraextraListView.as_view(), name='list_hora_extra'),
    path('ins/', HoraextraCreateView.as_view(), name='create_hora_extra'),
    path('upd/<int:pk>/', HoraextraUpdateView.as_view(), name='update_hora_extra'),
    path('del/<int:pk>/', HoraextraDeleteView.as_view(), name='delete_hora_extra'),
]