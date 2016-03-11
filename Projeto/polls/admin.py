from django.contrib import admin
from .models import Question, Choice

class InlineChoice(admin.TabularInline):
	model = Choice
	extra = 3
class AdminQuestion(admin.ModelAdmin):
	fieldsets = [
		(None,		{'fields': ['question_text']}),
		('Data',	{'fields': ['pub_date']}),
	]
	inlines = [InlineChoice]

admin.site.register(Choice)
admin.site.register(Question, AdminQuestion)