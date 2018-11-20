from django.db import models

# Create your models here.
class Image(models.Model):
    im = models.ImageField(upload_to='init/')