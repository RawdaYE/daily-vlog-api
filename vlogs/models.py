from django.db import models
from users.models import User

class Vlog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vlogs')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video_url = models.URLField()  # Or FileField if uploading
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author.username}"
