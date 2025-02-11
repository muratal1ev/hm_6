from django.shortcuts import render
from app.settings.models import Settings, Form
from django.views.generic import TemplateView, CreateView
from app.settings.forms import Forms
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     settings_id = Settings.objects.latest("id")
#     return render(request, 'base/index.html', locals())

class IndexView(CreateView):
    model = Form
    template_name = 'base/index.html'
    form_class = Forms
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings_id'] = Settings.objects.latest("id")
        return context


class ContactView(TemplateView):
    template_name = 'base/contact.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)