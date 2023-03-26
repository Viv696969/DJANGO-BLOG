from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField 

# Create your models here.




class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self): #afer submit button is clicked it will come here and will indirectly redirect to home
        return reverse('home')

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField(null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True , upload_to='images/profiles/')
    email=models.EmailField(blank=True,null=True,max_length=100)
    m_no=models.IntegerField(null=True,blank=True)
    sex=models.CharField(null=True,blank=True,max_length=500)
    website=models.CharField(null=True,blank=True,max_length=500)
    instagram=models.CharField(null=True,blank=True,max_length=500)
    twitter=models.CharField(null=True,blank=True,max_length=500)

     
    def __str__(self):
        return self.user.username


class Blog(models.Model):
    title=models.CharField(blank=False,max_length=100)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=100,default='sports')
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    body=RichTextField(blank=True,null=True)
    # body=models.TextField(blank=False)
    blog_crated=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='blog_likes')


    def totallikes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.author)+'|'+self.title

    def get_absolute_url(self): #afer submit button is clicked it will come here and will indirectly redirect to home
        return reverse('home')