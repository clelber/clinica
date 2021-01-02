from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario


class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.usuario = User.objects.create(
            username=funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        )
        funcionario.save()
        return super(FuncionarioCreateView, self).form_valid(form)


class FuncionariosListView(ListView):
    model = Funcionario

    def get_queryset(self):  # reescrita da queryset para filtrar pela empresa
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')




