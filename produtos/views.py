from django.views.generic import ListView, DetailView
from .models import Produto

class ProdutoListView(ListView):
    model = Produto

class ProdutoDetailView(DetailView):
    model = Produto
