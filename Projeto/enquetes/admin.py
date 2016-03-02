from django.contrib import admin
from .models import Pergunta, Escolha

class EscolhaInline(admin.TabularInline):
	model = Escolha
	extra = 3
class PerguntaAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,		{'fields': ['texto_pergunta']}),
		('Data',	{'fields': ['data_pub']}),
	]
	inlines = [EscolhaInline]

admin.site.register(Escolha)
admin.site.register(Pergunta, PerguntaAdmin)