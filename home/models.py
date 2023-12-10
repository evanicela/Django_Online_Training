from django.db import models

# Create your models here.

project_status = [
    ('level 1', 'level 1'),
    ('level 2', 'level 2'),
    ('level 3', 'level 3'),
]


class projects(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projectuploads')
    info = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    status = models.CharField(choices=project_status, max_length=50)
