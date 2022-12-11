from django.views.generic import CreateView

from .models import Convert
from .forms import ConvertForm
from .tasks import convert_and_send


class ConvertView(CreateView):
    model = Convert
    form_class = ConvertForm
    success_url = '/'
    template_name = 'index.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        # send_spam_email.delay(form.instance.email)
        # download_audio.delay(form.instance.yt_url)
        convert_and_send.delay(form.instance.pk)
        return super().form_valid(form)
