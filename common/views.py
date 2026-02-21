from django.shortcuts import render

from django.views.generic import TemplateView, FormView


class HomePageView(TemplateView):
    template_name = 'common/home-page.html'

