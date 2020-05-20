from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Message
from django.contrib.auth.models import User

class MessageCreateView(CreateView):
    model = Message
    fields = ['content', 'file_name']
    template_name = 'msgs/create_message.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.sender = self.request.user # przypisuje id zalogowanego usera do autora
        receiver = User.objects.get(id=self.kwargs['receiver_id'])
        form.instance.receiver = receiver
        return super().form_valid(form)

class ReceivedMessagesListView(ListView):
    model = Message
    template_name = 'msgs/inbox.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user)