from django.db import models

# Create your models here.

class Scrapers(models.Model):
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=254, default = 'scraper_users')     
    auth_token = models.CharField(max_length=254 , unique=True)

    def __str__(self):
        return self.username