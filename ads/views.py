from django.shortcuts import render, redirect
from .models import Ad
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context = {
        'ads': Ad.objects.all(),
        'title': 'Home Page',
    }
    return render(request, 'ads/home.html', context)

class AdListView(ListView):
    model = Ad
    template_name = 'ads/home.html' # <app>/<object>_<typeOfView> - tutaj - ads/ad_list
    context_object_name = 'ads'
    ordering = ['-date_posted']

class AdDetailView(DetailView):
    model = Ad

class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    fields = ['title', 'content', 'category']
    template_name = 'ads/ad_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user # przypisuje id zalogowanego usera do autora
        return super().form_valid(form)

class AdUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ad
    fields = ['title', 'content', 'category']
    template_name = 'ads/ad_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user # przypisuje id zalogowanego usera do autora
        return super().form_valid(form)

    def test_func(self): # sprawdzenie czy zalogowany user jest autorem ogłoszenia, wymaga UserPassesTestMixin
        ad = self.get_object()
        if self.request.user == ad.author:
            return True
        return False

class AdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ad
    template_name = 'ads/ad_delete.html'
    success_url = '/' # gdzie ma przekierować po usunięciu, w tym przypadku homepage

    def test_func(self): # sprawdzenie czy zalogowany user jest autorem ogłoszenia, wymaga UserPassesTestMixin
        ad = self.get_object()
        if self.request.user == ad.author:
            return True
        return False

def about(request):
    return render(request, 'ads/about.html')

# Create your views here.
