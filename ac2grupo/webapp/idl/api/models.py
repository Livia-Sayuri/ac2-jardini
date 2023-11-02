from django.db import models

# Create your models here.
# idl/api/models.py
from django.db import models

class Hotel(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=[('baratos', 'Baratos'), ('economicos', 'Econ�micos'), ('luxo', 'Luxo')])
    tipo_quarto = models.CharField(max_length=20, choices=[('simples', 'Simples'), ('dupla', 'Dupla'), ('duas_simples', 'Duas Simples')])
    centro_turistico = models.CharField(max_length=50, choices=[('S�o Paulo', 'S�o Paulo'), ('Rio de Janeiro', 'Rio de Janero'), ('Recife', 'Recife')])
    # Outros campos relevantes para o seu hotel, como pre�o, descri��o, etc.

    def __str__(self):
        return self.nome
