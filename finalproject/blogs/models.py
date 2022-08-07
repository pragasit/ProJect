from django.db import models
from .validators import file_size

# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="Videos/%y",validators=[file_size])
    def __str__(self):
        return self.caption
