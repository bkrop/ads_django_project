from django.shortcuts import render
from django.views.generic import CreateView
from .models import Message

class MessageCreateView(CreateView):
    model = Message
    fields = ['content']
    template_name = 'msgs/create_message.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.sender = self.request.user # przypisuje id zalogowanego usera do autora
        return super().form_valid(form)