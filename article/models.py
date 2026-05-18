from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="Kateqoriya adi")

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, verbose_name="Yazar"
    )
    title = models.CharField(max_length=150, verbose_name="Başlıq")  # input
    content = models.TextField(verbose_name="Məzmun")  # textarea
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    created_date = models.DateTimeField(auto_now_add=True)
    # image = models.FileField(upload_to="Article Images",blank=True, null=True,verbose_name="Şəkil")

    def __str__(self):
        return f"{self.title} | {self.author}"


class Comment(models.Model):
    author = models.CharField(max_length=30, verbose_name="Commentin Yazari")
    content = models.TextField(max_length=500, verbose_name="Comment")
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Meqaleler",
    )

    def __str__(self):
        return f"{self.author} | {self.content}"
