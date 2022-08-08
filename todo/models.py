from django.db import models

# Create your models here.

# ---------------------------------------------------------------------------- #
#                           model of the todo detail                           #
# ---------------------------------------------------------------------------- #

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'todo'
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ['-created_at']