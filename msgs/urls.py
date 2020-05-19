from django.urls import path
from .views import MessageCreateView


urlpatterns = [
    path('create/<int:receiver>', MessageCreateView.as_view(), name='message-create'),

]