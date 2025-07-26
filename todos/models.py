from django.db import models

# Create your models here.
# apps/todos/models.py
from django.db import models
from common.models import AuditModelMixin


class Todo(AuditModelMixin):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
