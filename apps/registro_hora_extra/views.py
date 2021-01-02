from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHoraExtra

"""
class HoraextraCreateView(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'horas']

    def form_valid(self, form):
        registro_horaextra = form.save(commit=False)
        registro_horaextra.funcinario = self.request.user.funcionario.id

        registro_horaextra.save()
        return super(HoraextraCreateView, self).form_valid(form)

"""


class HoraextraListView(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):  # reescrita da queryset para filtrar pela empresa
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


"""
class HoraextraUpdateView(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'horas']


class HoraextraDeleteView(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

"""




