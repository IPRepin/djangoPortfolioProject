from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateField()
    description = models.TextField(max_length=200)
    count = models.Fo

    def __str__(self):
        return self.title