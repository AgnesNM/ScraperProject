from django.db import models

# Create your models here.

class Scrapers(models.Model):
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=254, default = 'scraper_users')     
    auth_token = models.CharField(max_length=254 , unique=True)

    def __str__(self):
        return self.username
    
class Tshirt(models.Model):
    tshirt_id = models.IntegerField()
    size = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    fabric = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    defective = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.size} {self.color} {self.fabric}"

# class Sales(models.Model):
#     tshirt_id = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     date_sold = models.DateField()

#     def __str__(self):
#         return f"{self.tshirt_id} {self.price} {self.date_sold}"
    