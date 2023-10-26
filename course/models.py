from django.db import models

# Create your models here.

class Shop(models.Model):
    shopName = models.CharField(max_length=200, unique = True, verbose_name = "liste course name")
    # contains = models.SET( value=[])
    
    def __str__(self):
        return self.shopName


class Article(models.Model):
    articleName = models.CharField(max_length = 200, unique=True, verbose_name = "Nom de l'article")
    quantity = models.IntegerField(default = 1)
    description = models.CharField(max_length=2000, verbose_name="desciption")
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.articleName