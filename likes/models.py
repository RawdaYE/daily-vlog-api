from django.db import models
from users.models import User
from vlogs.models import Vlog
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vlog = models.ForeignKey(Vlog, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'vlog')

    def __str__(self):
        return f"{self.user} liked {self.vlog}"