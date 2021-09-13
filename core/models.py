from django.db import models

# Create your models here.

class Usuario(models.Model):
	login = models.CharField(max_length=25, primary_key=True)
	email = models.EmailField()
	nome = models.CharField(max_length=25)
	departamento = models.CharField(max_length=25)

	def __str__(self):
		return self.nome

class Chamado(models.Model):
	numero = models.IntegerField(primary_key=True)
	titulo = models.CharField(max_length=25)
	descricao = models.TextField(null=True)
	data = models.DateTimeField()
	tecnico = models.CharField(max_length=15)
	prioridade = models.CharField(max_length=15, null=True)
	status = models.CharField(max_length=15, null=True)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo