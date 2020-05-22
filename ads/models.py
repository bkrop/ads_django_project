from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Ad(models.Model):
    CATEGORIES_CHOICES = [
        ('Cars', 'Cars'),
        ('Work', 'Work'),
        ('Animals', 'Animals'),
        ('Electronics', 'Electronics'),
        ('Sport', 'Sport'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORIES_CHOICES)
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #usunięcie usera usunie jego posty
    image = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self): # służy do wygenerowania linku po utworzeniu ogłoszenia i przekierowaniu do niego
        return reverse('ad-detail', kwargs={'pk': self.pk})
