from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,blank=True,default='admin@gmail.com') 
    address = models.CharField(max_length=200,blank=True,default='Dhaka,Bangladesh')
    about = models.TextField()
    phone = models.CharField(max_length=15,blank=True,default='01234567890')
    logo = models.ImageField(upload_to='site/',blank=True,default='site/default_logo.png')
    about_img = models.ImageField(upload_to='site/',blank=True,default='site/default_about.png')
    facabook = models.CharField(max_length=100,blank=True,default='#')
    twitter = models.CharField(max_length=100,blank=True,default='#')
    instagram = models.CharField(max_length=100,blank=True,default='#')
    linkedin = models.CharField(max_length=100,blank=True,default='#')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Info'
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    cretaed_at = models.DateTimeField(auto_now_add=True)
    
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
    
