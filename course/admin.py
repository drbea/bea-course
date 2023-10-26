from django.contrib import admin

from course.models import Article, Shop

# Register your models here.


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("shopName",)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("articleName", "quantity", "shop", "description")

    # filtrer selon un certain nombre d'enregistrement
    list_filter = ["shop"]
    search_fields = ["articleName"]

    """ajouter de la pagination pour ne pas afficher tous les
    elements sur une seule page"""
    list_per_page = 5


