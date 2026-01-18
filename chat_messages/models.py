from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='messages')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def envoie(self):
        return f"Message from {self.sender} at {self.date}: {self.content}"
    
    

    