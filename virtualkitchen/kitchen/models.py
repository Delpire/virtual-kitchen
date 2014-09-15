from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=25)
  email = models.CharField(max_length=200)
  password = models.CharField(max_length=25)
  
  def __str__(self):
    return self.username_text
  
class Inventory(models.Model):
  user = models.ForeignKey(User)
  
class Recipe(models.Model):
  inventory = models.ForeignKey(Inventory)
  name = models.CharField(max_length=25)
  
  def __str__(self):
    return self.name_text

class Item(models.Model):
  inventory = models.ForeignKey(Inventory)
  recipe = models.ForeignKey(Recipe)
  name = models.CharField(max_length=25)
  type = models.CharField(max_length=25)
  amount = models.IntegerField(default=1)
  unit = models.CharField(max_length=25)
  
  def __str__(self):
    return self.name_text

