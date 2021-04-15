from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-timestamp",)

    def __str__(self):
        return f"{self.user} - {self.message}"
