from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Author" )
    title = models.CharField(max_length=50)
    """ title = models.CharField(max_length=50, verbose_name = "Başlık") """
    content = RichTextField() 
    """content = models.TextField(verbose_name = "İçerik")  """
    article_image = models.FileField(blank = True, verbose_name = "Add photograph in the article", null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name = "Created Date" )
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Articles", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="Name")
    comment_content = models.CharField(max_length=200, verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
# Create your models here.
