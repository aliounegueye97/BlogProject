from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'blog_app/article_list.html'
    context_object_name = 'articles'
    paginate_by = 6
    
    def get_queryset(self):
        return Article.objects.all()

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog_app/article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog_app/article_form.html'
    fields = ['titre', 'contenu', 'auteur', 'image']
    success_url = reverse_lazy('article-list')
    
    def form_valid(self, form):
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'blog_app/article_form.html'
    fields = ['titre', 'contenu', 'auteur', 'image', 'date_publication']
    success_url = reverse_lazy('article-list')

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'blog_app/article_confirm_delete.html'
    success_url = reverse_lazy('article-list')