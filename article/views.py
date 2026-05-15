from django.shortcuts import render
from .models import Article

# Create your views here.


def home__view(request):
    return render(request, "index.html")


# domain/articles/
def articles__view(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


# domain/article/1
def article__detail__view(request, id):
    article = Article.objects.get(id=id)
    return render(request, "article_detail.html", {"article": article})
