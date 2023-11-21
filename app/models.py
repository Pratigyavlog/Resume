from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=15)
    description=models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name=models.CharField(max_length=50)
    
    describe=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='projects', blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    github_link=models.URLField(max_length=500,blank=True)

    def __str__(self):
        return self.name
    
from django.db import models

class About(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField(max_length=1000)
    birthday = models.DateField()  # Assuming birthday is a date field
    phone = models.CharField(max_length=15)  # Assuming phone is a string with a maximum length of 15 characters
    city = models.CharField(max_length=100)  # Assuming city is a string with a maximum length of 100 characters
    age = models.IntegerField()  # Assuming age is an integer
    degree = models.CharField(max_length=100)  # Assuming degree is a string with a maximum length of 100 characters
    email = models.EmailField()  # Assuming email is an email field
    extracurricular=models.TextField(max_length=1000,blank=True)

    def __str__(self):
        return self.title
    
  