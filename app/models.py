from django.db import models
class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null= False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    remuneração = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)