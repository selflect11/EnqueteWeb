#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.urlresolvers import reverse
from django.utils import timezone
from Projeto import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm
from .models import Question, Choice

def Login(request):
	Next = request.GET.get('next', '/')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(Next)
			else:
				HttpResponse("Inactive user")
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)
	uf = UserForm() 
	return render(request, 'polls/login.html', {'redirect_to' : Next, 'form' : uf})

def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

@login_required(login_url='/login/')
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {'latest_question_list' : latest_question_list}
	return render_to_response('polls/index.html', context)

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())

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

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.filter(pub_date=timezone.now()).order_by('-pub_date')[:5]