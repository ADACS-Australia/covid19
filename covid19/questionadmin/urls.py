from django.shortcuts import render

# Create your views here.

from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='front-page.html')),
    path('questionnaire', views.IndexView.as_view(), name='questionnaire'),
    path('saveresponse', views.QuestionnaireView.home, name='saveresponse'),
    path('<int:question_id>/', views.ScaleView.as_view(), name='form'),
]
