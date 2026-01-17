from django.db import models

# Create your models here.

class Message(models.Model):
    sender = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def envoie(self):
        return f"Message from {self.sender} at {self.date}: {self.content}"
    
    

    