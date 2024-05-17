from django.db import models
from user.models import CustomUser

class Blogs(models.Model):
    title = models.CharField(max_length=40)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True )
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    isDeleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    

    
