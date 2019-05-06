from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
  template_name = 'single_monitor/index.html'

  def get_queryset(self):
    pass


class PingView(LoginRequiredMixin, generic.ListView):
  template_name = 'single_monitor/ping.html'

  def get_queryset(self):
    pass


class PortView(LoginRequiredMixin, generic.ListView):
  template_name = 'single_monitor/port.html'

  def get_queryset(self):
    pass


class UrlView(LoginRequiredMixin, generic.ListView):
  template_name = 'single_monitor/url.html'

  def get_queryset(self):
    pass


class DnsView(LoginRequiredMixin, generic.ListView):
  template_name = 'single_monitor/dns.html'

  def get_queryset(self):
    pass

class DomainView(LoginRequiredMixin, generic.ListView):
  template_name = 'single_monitor/domain.html'

  def get_queryset(self):
    pass


class CertView(LoginRequiredMixin, generic.ListView):
  template_name = 'single_monitor/cert.html'

  def get_queryset(self):
    pass


