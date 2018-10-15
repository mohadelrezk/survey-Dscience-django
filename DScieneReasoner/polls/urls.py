from django.conf.urls import url

from . import views

urlpatterns = [

    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<question_id>)/$', views.detail, name='detail'),

    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/survey/
    url(r'^survey/$', views.survey, name='survey'),

    # ex: /polls/thanks/
    url(r'^thanks/$', views.thanks, name='thanks'),

    # ex: /polls/get_answer/
    url(r'^(?P<question_id>[0-9]+)/get_answer/$', views.get_answer, name='get_answer'),
]

