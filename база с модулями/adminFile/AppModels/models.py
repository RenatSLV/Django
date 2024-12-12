from django.db import models
from AppModels.validators import *
# Create your models here.

class IceCreamShop(models.Model):
    id_shop = models.IntegerField(auto_created=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    popolarity = models.IntegerField(null=True, blank=True)
    opening_hours = models.CharField(max_length=20)
    contact_info = models.TextField(null=True, blank=True)
    owner = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Киоск с мороженым"
        verbose_name_plural = "Киоски с мороженым"

    def __str__(self):
        return self.name


class IceCream(models.Model):
    name = models.CharField(max_length=100)
    ShopId = models.ForeignKey('IceCreamShop', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Мороженое"
        verbose_name_plural = "Мороженые"

    def __str__(self):
        return self.name


class Parent(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    
    class Mete:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'
    
    def __str__(self):
        return  self.name
    

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'
    
    def __str__(self):
        return self.name

class News(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(validators=[validate_more_zero])
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title