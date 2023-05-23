
from django.contrib import admin
from django.urls import path

from produtos.views import ProdutoListView, ProdutoDetailView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ProdutoListView.as_view(), name='listar_produtos'),
    path('produtos/<int:pk>/', ProdutoDetailView.as_view(), name="detalhar_produto"),
    path('admin/', admin.site.urls),
]
