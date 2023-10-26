from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
import datetime


from course.models import Article, Shop
from course.form import ArticleForm, ShopForm, LoginForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valide():
            return redirect("course/acceuil.html")
        else:
            form = LoginForm()
    else:
        form = LoginForm()
    
    context = {"form": form,
               "shoplist": Shop.objects.all,
               "articles": Article.objects.all
               }

    return render(request, "course/acceuil.html", context)


def show_profile(request):
    context = {
        "name": "bea"
    }
    return render(request, "course/profiles/user-profile.html", context)


#@permission_required("mangalib.add_article", raise_exception = True) 
def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("course:index")
    else:
        form = ArticleForm

    context = {"form": form}
    return render(request, "course/article-form.html", context)

#@permission_required("mangalib.add_shop", raise_exception = True) 
def add_shoplist(request):
    if request.method == "POST":
        form = ShopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("course:index")
    else:
        form = ShopForm

    context = {"form": form}
    return render(request, "course/shop-form.html", context)


#@permission_required("mangalib.change_article", raise_exception = True)  # <app_name>.<action>_modelName
def updateArticleName(request, article_id):
    article = Article.objects.get(pk = article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance = article)

        if form.is_valid():
            form.save()
            return redirect("course:index")
    else:
        form = ArticleForm(instance = article)

    context = {"form": form}
    return render(request, "course/article-form.html", context)


#@permission_required("mangalib.delete_article", raise_exception = True)  # <app_name>.<action>_modelName
def delete_article(request, article_id):
    article = Article.objects.get(pk = article_id)  
    article.delete()
    return redirect("course:index")


#@permission_required("gestioncourse.view_article", raise_exception = True)  # <app_name>.<action>_modelName
def show_article(request, article_id):
    context = {
        "article": get_object_or_404(Article, pk = article_id)
    }
    return render(request, "course/show-article.html", context)
