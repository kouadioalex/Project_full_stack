from django.db import models

class Article(models.Model):
    image= models.ImageField(default="paris.jpg")
    titre= models.CharField(max_length=150)
    date_publication=models.DateTimeField(auto_now=True)
    slug= models.SlugField(max_length=150)
    contenu= models.TextField()
    
    def __str__(self):
        return self.titre
    
    
    