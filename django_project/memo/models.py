from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_notified = models.BooleanField(default=False)

    def __str__(self):
        return self.title