from django.db import models
from users.models import User
from vlogs.models import Vlog
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    vlog = models.ForeignKey(Vlog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.vlog.title}"
