from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from article.models import Article,Comment
from .forms import ArticleForm



""" urls.py den yönlenecek olan fonksiyonu burada yazacaksin """
def addComment(request,id):
   article = get_object_or_404(Article, id=id)
   if request.method == "POST":
      comment_author = request.POST.get("comment_author")
      comment_content = request.POST.get("comment_content")
      newComment = Comment(comment_author = comment_author, comment_content = comment_content)
      newComment.article = article
      newComment.save()
   return redirect("/articles/article/" + str(id))



@login_required(login_url="/user/login/")
def articles(request):
   keyword = request.GET.get("keyword")
   if keyword:
      articles = Article.objects.filter(title__contains = keyword)
      return render(request, "articles.html",{"articles":articles})
   articles = Article.objects.all() #tüm articleları alarak listeye atıcak
   return render(request, "articles.html",{"articles":articles})
   
   
def index(request):
    context = {
        "number1":20,
        "number2":20,
        "numbers":[1,2,3,4,5,6]
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all() 
    return render(request,"detail.html",{"article": article, "comments":comments})

@login_required(login_url="/user/login/")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    """ Giriş yapmış kullanıcının articlelarını almak için filter kullandım """
    context = {
        "articles" : articles
    }
    return render(request, "dashboard.html",context)
""" def detail(request, id):
    return HttpResponse("Detail" + str(id))
    Dinamik url adreslerimizi bu şekilde tanımlarız
     """
# Create your views here.
@login_required(login_url="/user/login/")
def addArticle(request):
    form = ArticleForm(request.POST  or None, request.FILES or None)
    if form.is_valid():
     article =form.save(commit=False)
     article.author = request.user
     article.save()

     """Burada article objesini oluşturuyor ve sonra kaydediyor ancak yazar bilgisini girmediğimiz iiçin girmeden oluşturmaya çalışıyor bu yüzden integrity hatası alıyorum. save işlemini yapma ben yapıcmam dememiz için. Eğer author bilgimiz olmasaydı direk kaydolacaktı form.save() dediğimizde """
     messages.success(request,"Article created successfuly")
     return redirect("index")
    return render(request, "addArticle.html",{
        "form":form
    }
    )


@login_required(login_url="/user/login/")
def updateArticle(request, id):
  article = get_object_or_404(Article,id = id)
  form = ArticleForm(request.POST or None, request.FILES or None , instance = article)
  if form.is_valid():
      article =form.save(commit=False)
      article.author = request.user
      article.save()
      messages.success(request,"Article updated successfuly")
      return redirect("article:dashboard")
  
  return render(request, "update.html",{"form":form})

@login_required(login_url="/user/login/")
def deleteArticle(request, id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Article deleted")
    return redirect("article:dashboard")
