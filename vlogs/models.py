from django.db import models
from users.models import User

class Vlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vlogs")
    content = models.TextField()
    media_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
