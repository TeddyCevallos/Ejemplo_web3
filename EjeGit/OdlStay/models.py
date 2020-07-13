from django.db import models
from django.db.models import Model
# Create your models here.
class Article(Model):
    firtname = models.CharField(max_length = 15)
    lastname = models.CharField(max_length = 15)
    email = models.CharField(max_length = 30)
    date_ar = models.DateTimeField(auto_now_add = False)
    contexto = models.TextField(max_length = 999)

    def __str__(self):
        mostar = "{0} {1}"
        return mostar.format(self.firtname, self.lastname)

class User (Model):
    firstname = models.CharField(max_length = 15)
    lastname = models.CharField(max_length = 15)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 15)
    confirm_pass = models.CharField(max_length = 15)

    def __str__(self):
        mostar = "{0} {1}"
        return mostar.format(self.firtname, self.lastname)    
