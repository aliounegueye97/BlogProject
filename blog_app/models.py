from django.db import models # type: ignore
from django.urls import reverse # type: ignore
from django.utils import timezone # type: ignore

class Article(models.Model):
    titre = models.CharField(max_length=200, verbose_name="Titre")
    contenu = models.TextField(verbose_name="Contenu")
    date_publication = models.DateTimeField(default=timezone.now, verbose_name="Date de publication")
    auteur = models.CharField(max_length=100, verbose_name="Auteur")
    image = models.ImageField(upload_to='article_images/', blank=True, null=True, verbose_name="Image illustrative")
    
    class Meta:
        ordering = ['-date_publication']
        verbose_name = "Article"
        verbose_name_plural = "Articles"
    
    def __str__(self):
        return self.titre
    
    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})