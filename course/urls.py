from django.urls import path
from . import views

app_name = "course"

urlpatterns = [
    path("", views.index, name="index"),
    path("user-profil/", views.show_profile, name = "userprofil"),
    path("add-article/", views.add_article, name = "addarticle"),    
    path("<int:article_id>", views.show_article, name="showarticle"),  # manga/<id>
    path("add-shop/", views.add_shoplist, name = "addshop"),
    path("m-a-j/<int:article_id>/", views.updateArticleName, name = "updateArticleName"),
    path("delete-article/<int:article_id>/", views.delete_article, name = "delete_article")

]
