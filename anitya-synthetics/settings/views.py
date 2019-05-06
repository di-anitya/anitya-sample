from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
  template_name = 'settings/index.html'

  def get_queryset(self):
    pass
