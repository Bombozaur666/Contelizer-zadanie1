import re

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseBase
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from mixer.forms import MixerForm
from mixer.utils import shuffle_word


class UploadView(FormView):
    template_name = "mixer_form.html"
    form_class = MixerForm
    success_url = reverse_lazy('mixer-preview')

    def form_valid(self, form: MixerForm) -> HttpResponse:
        _file = form.cleaned_data['file']

        try:
            content = _file.read()
            content = content.decode('utf-8')
        except UnicodeDecodeError:
            form.add_error('file', 'UTF-8 required')
            return self.form_invalid(form)

        shuffled_content = re.sub(r'(\w+)', shuffle_word, content)

        self.request.session['text'] = shuffled_content
        return super().form_valid(form)

class ResultView(TemplateView):
    template_name = 'preview.html'

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponseRedirect | HttpResponseBase:
        if 'text' not in self.request.session:
            return redirect('mixer-upload')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['text'] = self.request.session.pop('text')
        return context