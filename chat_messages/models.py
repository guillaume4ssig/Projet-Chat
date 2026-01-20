from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Salon(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    role_list =   {
         ('adm', 'admin'),
         ('mem','membre')}
    user_role = models.CharField(max_length=50,choices=role_list,null=True)
    
    def __str__(self):
        return self.name


class Message(models.Model):
    salon = models.ForeignKey(
        Salon,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} : {self.content[:20]}"

    




    

    