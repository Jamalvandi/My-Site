from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Post (models.Model):
    # image
    author = models.ForeignKey(User, null= True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default= 0)
    state = models.BooleanField(default= False)
    published_date = models.DateTimeField(null= True)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)
    # all thing in Meta is generally
    class Meta:
        ordering = ["created_date"]
    def __str__(self):
        return "{} - {}".format(self.title, self.id)