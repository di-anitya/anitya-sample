from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
  template_name = 'security_monitor/index.html'

  def get_queryset(self):
    pass


class FalsificationView(LoginRequiredMixin, generic.ListView):
  template_name = 'security_monitor/falsification.html'

  def get_queryset(self):
    pass


class VulnerabilityView(LoginRequiredMixin, generic.ListView):
  template_name = 'security_monitor/vulnerability.html'

  def get_queryset(self):
    pass

