from django.db import models
from django.contrib.auth.models import User


class ChatLogs(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    query=models.TextField()
    answer=models.TextField(blank=True, null=True)
    time=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.query[:80]