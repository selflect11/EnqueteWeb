from django.db import models

class Pergunta(models.Model):
	texto_pergunta = models.CharField(max_length=200)
	data_pub = models.DateTimeField('data de publicação')
	def __str__(self):
		return self.texto_pergunta

class Escolha(models.Model):
	pergunta = models.ForeignKey(Pergunta)
	texto_escolha = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)
	def __str__(self):
		return self.texto_escolha
