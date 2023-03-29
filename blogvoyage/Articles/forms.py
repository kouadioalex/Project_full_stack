from django.forms import ModelForm
from .models import Article

class ArticleCreer(ModelForm):
    class Meta:
        model= Article
        fields= ['titre', 'slug', 'contenu', 'image']
        
