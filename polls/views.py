# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/index.html", context)
    # #output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))



def detail (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
        
#return HttpResponse("You're looking at question %s." % Question.objects.get(pk=question_id).__str__())

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse("reponse % question_id" % Question.objects.get(pk=question_id).__str__())

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.

