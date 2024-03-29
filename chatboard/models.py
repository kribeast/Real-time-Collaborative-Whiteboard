from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Group(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    members = models.ManyToManyField(User)

    def add_user(request, user):
        self.members.add(user)
        self.save()
        return
    
    def remove_user(request, user):
        self.members.remove(user)
        self.save()
        return

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    

    def __str__(self) -> str:
        return f'{self.author} => {self.content}'