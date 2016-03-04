from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world. Pagina de enquetes")
def detail(request, question_id):
	response = "Você está olhando os resultados da enquete %s"
	return HttpResponse(response % question_id)
def results(request, question_id):
	response = "Você está olhando os resultados da enquete %S"
	return HttpResponse(response % question_id)
def vote(request, question_id):
	response = "Você está votando na enquete %s"
	return HttpResponse(response % question_id)