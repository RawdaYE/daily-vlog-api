from django.db import models
from users.models import User
from vlogs.models import Vlog

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    vlog = models.ForeignKey(Vlog, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'vlog')  # A user can like a vlog only once

    def __str__(self):
        return f"{self.user.username} liked {self.vlog.title}"
