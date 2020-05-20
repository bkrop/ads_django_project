from django.urls import path
from .views import MessageCreateView, ReceivedMessagesListView


urlpatterns = [
    path('create/<int:receiver_id>', MessageCreateView.as_view(), name='message-create'),
    path('inbox', ReceivedMessagesListView.as_view(), name='inbox'),
]