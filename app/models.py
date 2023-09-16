from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,blank=True,default='admin@gmail.com') 
    about = models.TextField()
    phone = models.CharField(max_length=15,blank=True,default='01234567890')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Info'
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True,default='images/default.jpg')
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Movies'
    
