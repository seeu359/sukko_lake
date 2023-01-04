from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from sukko_lake.forms import CreateApplicationForm
from sukko_lake.models import Application, FakeFeedback, MainPicture
from sukko_lake.services.services import is_true_phone_number, send_alert_email
from sukko_lake.services.text import Messages


class MainPageView(TemplateView):

    template_name = 'base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['pics'] = MainPicture.objects.all()
        context['feedback'] = FakeFeedback.objects.all()
        context['form'] = CreateApplicationForm()
        return context


class CreateApplicationView(CreateView):
    model = Application
    form_class = CreateApplicationForm
    success_url = reverse_lazy('main')
    context_object_name = 'apps'
    template_name = 'base.html'

    def form_valid(self, form):
        """If form is valid, will be sent email and application will
        be added to database.
        Else - redirect to main page with error flash message"""
        name = form.cleaned_data['client_name']
        phone_number = form.cleaned_data['client_number']
        if is_true_phone_number(phone_number):
            messages.success(
                self.request, Messages.ApplicationComplete.value
            )
            send_alert_email(name, phone_number)
            self.object = form.save()
            return super().form_valid(form)
        messages.error(self.request, Messages.ApplicationError.value)
        return redirect('main')
