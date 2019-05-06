from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
  template_name = 'scenario_monitor/index.html'

  def get_queryset(self):
    pass


class StepView(LoginRequiredMixin, generic.ListView):
  template_name = 'scenario_monitor/step.html'

  def get_queryset(self):
    pass


class ApiView(LoginRequiredMixin, generic.ListView):
  template_name = 'scenario_monitor/api.html'

  def get_queryset(self):
    pass

