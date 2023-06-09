from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView, LoginView

app_name = 'autenticacao'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),

    #  LOGOUT AUTH DJANGO
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dados/<int:pk>/', views.DadosUsuario.as_view(), name='dados'),


    path('endereco/', views.EnderecoList.as_view(), name='endereco'),
    path('novo_endereco/', views.NovoEndereco.as_view(), name='novo_endereco'),
    path('delete_endereco/<int:pk>/', views.DeleteEndereco.as_view(), name='delete_endereco'),
    path('update_endereco/<int:pk>/', views.UpdateEndereco.as_view(), name='update_endereco'),

    path('endereco_padrao/<int:id>/', views.endereco_padrao, name='endereco_padrao'),

]
