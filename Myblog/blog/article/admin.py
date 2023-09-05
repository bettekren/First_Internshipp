from django.contrib import admin
from .models import Article,Comment

admin.site.register(Comment)
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
   
    class Meta:
        model = Article
  
    list_display = ["title", "author", "created_date", "content"]
    list_display_links = ['content']
    search_fields = ["content"]
    list_filter = ["title", "created_date"]
    










    
""" Meta isimli bu class django tarafindan söyleniyor özelleştirme için ismini değiştiremiyoruz """
""" ArticleAdmin class ını Article modeliyle  birleştirmem gerek. ArticleAdmin Article modelini özelleştirecek""" 