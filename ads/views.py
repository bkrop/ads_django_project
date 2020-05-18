from django.shortcuts import render, redirect, get_object_or_404
from .models import Ad
from .forms import SearchForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q


class AdListView(ListView):
    model = Ad
    template_name = 'ads/home.html' # <app>/<object>_<typeOfView> - tutaj - ads/ad_list
    context_object_name = 'ads'
    ordering = ['-date_posted']
    extra_context = {'categories': Ad.CATEGORIES_CHOICES}
    form_class = SearchForm

class AdSearchView(ListView):
    model = Ad
    template_name = 'ads/ad_search.html'
    context_object_name = 'ads'
    
    def get_queryset(self):
        query = self.request.GET.get('q') # bierze tekst z form gdzie name='q'
        ads = Ad.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) # wrzuca tekst i wyszukuje wszystko co jest w tytule LUB content, stąd |
        )
        return ads

class AdFilteredListView(ListView):
    model = Ad
    template_name = 'ads/filtered.html'
    context_object_name = 'ads'

    def get_queryset(self):
        return Ad.objects.filter(category=self.kwargs.get('category')).order_by('-date_posted')

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
