# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
#or
from django.shortcuts import render, get_object_or_404,  get_list_or_404
from django.http import Http404

from django.urls import reverse


from .models import Question, Choice


def index(request):
    introduction_message = 'survey introduction message'
    #template = loader.get_template('polls/index.html')
    #context = {
    #    'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))
    #or
    context = {'introduction_message': introduction_message}
    return render(request, 'polls/index.html', context)

def survey(request):
    #@TODO: get question and its possible answers and send to the voting form
    list_of_questions = [] #get form database
    #list_of_prevouse_answers = [] #get from database
    random_question = "You're voting on my questions %s." % 'x'
    context = {'random_question': random_question} #, 'list_of_prevouse_answers': list_of_prevouse_answers}
    return render(request, 'polls/survey.html', context)
    #return HttpResponse()

def get_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def thanks(request):
    thanks_message = "thanks for voting on my questions %s." % 'x'
    context = {'thanks_message': thanks_message}
    return render(request, 'polls/thanks.html', context)
    #return HttpResponse()




#@TODO

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        # get_list_or_404()
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

#@TODO
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
