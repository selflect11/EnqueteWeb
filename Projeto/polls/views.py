from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from .models import Question, Choice


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {'latest_question_list' : latest_question_list}
	return HttpResponse(template.render(context, request))

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
            })
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))