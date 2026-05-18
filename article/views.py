from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.


def home__view(request):
    return render(request, "index.html")


# domain/articles/
def articles__view(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


# domain/article/1
def article__detail__view(request, id):
    # comment = Comment.objects.
    # article = Article.objects.get(id=id)
    article = Article.objects.get(id=id)
    comments = article.comments.all()
    category = article.category

    context = {"article": article, "comments": comments, "category": category}
    return render(request, "article_detail.html", context)


def add__article__view(request):
    if not request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("articles")

    else:
        form = ArticleForm()

    return render(request, "article_form.html", {"form":form})