from django import forms
from .models import Shop, Article


class ShopForm(forms.ModelForm):
    shopName = forms.CharField(label = "Nom de la liste de course", max_length = 100)
    
    class Meta:
        model = Shop
        fields = ["shopName"]


class ArticleForm(forms.ModelForm):
    shop = forms.ModelChoiceField(queryset= Shop.objects.all(), label= "listes de course")
    
    class Meta:
        model = Article
        fields = ["articleName", "quantity", "shop", "description"]


class LoginForm(forms.Form):
    firstname = forms.CharField(label = "First Name", max_length = 50)
    firstname = forms.CharField(label = "First Name", max_length = 50)
    email = forms.EmailField(label = "email", max_length = 50)
 

        