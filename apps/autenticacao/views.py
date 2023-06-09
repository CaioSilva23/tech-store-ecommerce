from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import EnderecoForm, RegisterForms, DadosUsuarioForm
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Endereco, DadosUsuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404


class Cadastro(CreateView):
    form_class = RegisterForms
    template_name = 'register.html'
    success_url = reverse_lazy('autenticacao:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(self.request, 'Cadastro realizado com sucesso!')
        return super().form_valid(form)


class DadosUsuario(LoginRequiredMixin, UpdateView):
    template_name = 'perfil.html'
    model = DadosUsuario
    form_class = DadosUsuarioForm

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.get_object().pk != self.request.user.dadosusuario.pk:
            raise Http404()
        return super().get(request, *args, **kwargs)

    def get_success_url(self) -> str:
        messages.success(self.request, 'Perfil editado com sucesso!')
        return reverse_lazy('autenticacao:dados', kwargs={'pk': self.get_object().pk})


class EnderecoList(LoginRequiredMixin, ListView):
    template_name = 'endereco.html'
    model = Endereco
    context_object_name = 'enderecos'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['enderecos'] = Endereco.objects.filter(user=self.request.user)
        return ctx


class UpdateEndereco(LoginRequiredMixin, UpdateView):
    model = Endereco
    form_class = EnderecoForm
    template_name = 'form_endereco.html'
    success_url = reverse_lazy('autenticacao:endereco')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Endereço atualizado com sucesso!')
        return super().form_valid(form)


class NovoEndereco(LoginRequiredMixin, CreateView):
    model = Endereco
    form_class = EnderecoForm
    template_name = 'form_endereco.html'
    success_url = reverse_lazy("autenticacao:endereco")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        endereco = form.save(commit=False)
        endereco.user = self.request.user
        endereco.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, 'Novo endereço adicionado com sucesso.')
        return super().get_success_url()


class DeleteEndereco(LoginRequiredMixin, DeleteView):
    model = Endereco
    success_url = reverse_lazy('autenticacao:endereco')

    def get_success_url(self) -> str:
        messages.success(self.request, 'Endereço deletado com sucesso!')
        return super().get_success_url()


from django.shortcuts import redirect

def endereco_padrao(request, id):
    padrao_antigo = Endereco.objects.filter(padrao=True).first()
    if padrao_antigo:
        padrao_antigo.padrao = False
        padrao_antigo.save()

    novo_padrao = Endereco.objects.get(id=id)
    novo_padrao.padrao = True
    novo_padrao.save()
    return redirect('autenticacao:endereco')

