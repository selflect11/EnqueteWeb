#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from polls.views import DetailView, ResultsView

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'(?P<pk>[0-9]+)/$',
		DetailView.as_view(), name='detail'),
	url(r'(?P<pk>[0-9]+)/results/$',
		ResultsView.as_view(), name='results'),
	url(r'(?P<question_id>[0-9]+)/vote/$',
		views.vote, name='vote')
]