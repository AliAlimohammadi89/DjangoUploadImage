from django.db import models
# from .models import Image

# Create your models here.
class Image (models.Model):
    countofpic = models.IntegerField(verbose_name='cont of pictors ',default=3)
    image = models.ImageField(upload_to='images',verbose_name='as')

    def __str__(self):
        return self.countofpic