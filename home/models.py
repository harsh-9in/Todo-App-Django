from django.db import models

# Create your models here.
class todo_item(models.Model):
    content=models.TextField()