from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# ---------------------------------------------------------------------------- #
#                           model of the memo detail                           #
# ---------------------------------------------------------------------------- #

class MemoUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

class Memo(models.Model):
    user = models.ForeignKey(MemoUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'memo'
        verbose_name = 'Memo'
        verbose_name_plural = 'Memos'
        ordering = ['-created_at']