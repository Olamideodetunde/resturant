from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname= models.CharField(max_length=100)
    email_add=models.EmailField(max_length=254)
    phone=models.CharField(max_length=100)
    message=models.TextField(max_length=300)
    def __str__(self) :
     return f'{self.fullname}  {self.phone}'
class Menu(models.Model):
    class FoodTypeChoices(models.TextChoices):
        BREAKFAST='breakfast'
        LUNCH='lunch'
        DINNER='dinner'
    food_name= models.CharField(max_length=100)
    food_type= models.CharField(max_length=100,null=True,choices=FoodTypeChoices.choices)
    food_price =models.FloatField(max_length=10)
    food_image=models.ImageField(max_length=200,upload_to='foods/')
    rating=models.IntegerField()
    def __str__(self) :
        return f'{self.food_name}  {self.food_price}'
class Reservation(models.Model):
    name=models.CharField(max_length=100)
    email_add=models.EmailField(max_length=254)
    phone=models.CharField(max_length=100)
    no_of_persons=models.IntegerField()
    date_reserved=models.DateField()
    time_reserved=models.TimeField()
    special_requests= models.TextField(max_length=500)
    def __str__(self) :
        return f'{self.name}  {self.date_reserved}'
class News(models.Model):
    class NewsTagChoices(models.TextChoices):
        FEATURED='featured'
        PROMOTIONS='promotions'
        CAREER='career'
        MEETING='meeting'
    news_title=models.CharField(max_length=300)
    news_image=models.ImageField(max_length=200,upload_to='news/')
    news_date=models.DateField(auto_now=True)
    news_tag=models.CharField(max_length=50,null=True,choices=NewsTagChoices.choices)
    news_slug=models.CharField(max_length=200,null=True)
    def __str__(self) :
        return f'{self.news_title}  {self.news_image}'
