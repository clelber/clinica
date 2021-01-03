from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .forms import RegistroHoraExtraForm
from .models import RegistroHoraExtra


class HoraextraCreateView(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraextraCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraextraListView(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):  # reescrita da queryset para filtrar pela empresa
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraextraUpdateView(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']


class HoraextraDeleteView(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')






