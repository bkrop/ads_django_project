from django.urls import path
from . import views
from .views import AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, AdFilteredListView, AdSearchView

urlpatterns = [
    path('', AdListView.as_view(), name='ads-home'),
    path('<str:category>', AdFilteredListView.as_view(), name='ads-filtered'),
    path('about/', views.about, name='ads-about'),
    path('ad/<int:pk>', AdDetailView.as_view(), name='ad-detail'),
    path('ad/create', AdCreateView.as_view(), name='ad-create'),
    path('ad/search/', AdSearchView.as_view(), name='ad-search'),
    path('ad/update/<int:pk>', AdUpdateView.as_view(), name='ad-update'),
    path('ad/delete/<int:pk>', AdDeleteView.as_view(), name='ad-delete'),
]
