from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()

    def __str__(self) -> str:
        return f'{self.nome} - {self.preco}'