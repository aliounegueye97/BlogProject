from django.contrib import admin # type: ignore
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')
    list_filter = ('date_publication', 'auteur')
    search_fields = ('titre', 'contenu', 'auteur')
    date_hierarchy = 'date_publication'
    ordering = ['-date_publication']
    fieldsets = (
        ('Informations principales', {
            'fields': ('titre', 'contenu', 'auteur')
        }),
        ('Publication', {
            'fields': ('date_publication', 'image')
        }),
    )